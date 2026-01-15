from langchain.messages import SystemMessage, HumanMessage

from investment_assistant.states import InterviewState
from investment_assistant.utils.models import model, cheap_model
from investment_assistant.prompts.question_generation import ask_question_prompt, search_query_prompt


async def generate_search_query(messages):
    interview = ""
    for i, message in enumerate(messages):
        role = 'Analyst' if i % 2 == 0 else 'Expert'
        interview += f'{role}: {message.content}\n\n'

    result = await model.ainvoke([SystemMessage(content=search_query_prompt), HumanMessage(content=interview) ])

    return result.content


async def generate_question(state: InterviewState) -> InterviewState:
    """ Node to generate a question by analyst agent and derive search query from it """

    analyst = state.analyst
    company = state.company
    messages = state.interview_messages

    # Generate question 
    system_message = ask_question_prompt.format(goals=analyst, company=company)
    question = await model.ainvoke([SystemMessage(content=system_message)]+messages)

    # Generate search query for web search
    search_query = await generate_search_query([*state.interview_messages[1:], question])

    return {
        "interview_messages": [question],
        "search_query": search_query
        }
