from langchain.messages import SystemMessage, HumanMessage
from langfuse import observe

from app.investment_assistant.utils.models import llm_call
from app.investment_assistant.states import InterviewState
from app.investment_assistant.prompts.answer_generation import system_prompt
from app.investment_assistant.utils.data_processing import swap_message_roles


@observe
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
    answer = await llm_call([SystemMessage(content=system_message), *messages])
    
    # Log expert answer to terminal
    print(f"\n{'='*60}")
    print(f"🧠 EXPERT: {answer.content[:500]}{'...' if len(answer.content) > 500 else ''}")
    print(f"{'='*60}")

    # Append the response as human message so that Analyst understands it's from the human expert
    answer = HumanMessage(content=answer.content)
    answer.name = "expert"  # to track number of interview turns
    
    return {"interview_messages": [answer]}
