from langchain.messages import SystemMessage, HumanMessage

from investment_assistant.states import ResearchStateWithMessage
from investment_assistant.utils.models import model
from investment_assistant.prompts.finalize_report import system_prompt

async def final_report(state: ResearchStateWithMessage):
    """ Reduce phase where we combine all the separate reports given by all analysts """

    reports = state.sections
    prompt = f"Here are {len(reports)} reports:\n"
    for i, report in enumerate(reports):
        prompt += f"REPORT {i + 1}:\n\n{report}\n\n"

    result = await model.ainvoke([SystemMessage(content=system_prompt), HumanMessage(content=prompt)])

    return {"messages": [result]}