from langchain.messages import SystemMessage, HumanMessage, AIMessage

from investment_assistant.utils.models import model
from investment_assistant.states import InterviewState
from investment_assistant.prompts.answer_generation import system_prompt
from investment_assistant.utils.data_processing import swap_message_roles


async def generate_answer(state: InterviewState):
    """ Node to answer a question """

    analyst = state.analyst
    company = state.company
    context = state.context

    messages = swap_message_roles(state.interview_messages)

    # Answer question
    system_message = system_prompt.format(
        goals=analyst.persona,
        context=context,
        company=company
        )
    answer = await model.ainvoke([SystemMessage(content=system_message), *messages])

    # Append the response as human message so that Analyst understands it's from the human expert
    answer = HumanMessage(content=answer.content)
    answer.name = "expert"  # to track number of interview turns
    
    return {"interview_messages": [answer]}
