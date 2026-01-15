from langchain.messages import HumanMessage, SystemMessage, AIMessage
from pydantic import BaseModel, Field

from investment_assistant.states import ResearchStateWithMessage, ResearchState
from investment_assistant.utils.models import model, cheap_model
from investment_assistant.utils.web_search import search_engine
from investment_assistant.prompts.gather_company_info import company_name_extraction_prompt, structured_data_extraction_prompt


class CompanyNameOutput(BaseModel):
    company_name: str = Field(..., description="The name of the company extracted from the text.")

async def extract_company_name(messages):
    """ Extract company name from messages """

    model_with_structure = model.with_structured_output(CompanyNameOutput)
    result = await model_with_structure.ainvoke([SystemMessage(content=company_name_extraction_prompt), *messages])
    
    return result.company_name


async def search_company_info(company_name: str):
    """ Search web for company information """

    search_result = await search_engine.ainvoke({"query": f"Is {company_name} a public company? which country does it belong to? if it is traded publicly what is the stock symbol(If in india get symbol of NSE)? In what sectors does it operate?"})
    return search_result['answer']     # Summary of web search


async def gather_info(state: ResearchStateWithMessage) -> ResearchStateWithMessage:
    """ Gathers company information from web and updates the research state. """

    messages = state.messages
    company_name = await extract_company_name(messages)
    web_search_result = await search_company_info(company_name)

    # Extract structured data from web search
    model_with_structure = model.with_structured_output(ResearchState)
    extracted_model = await model_with_structure.ainvoke([SystemMessage(content=structured_data_extraction_prompt), HumanMessage(content=web_search_result)])
    
    confirmation_message = web_search_result + '\n\n Did you mean this company?'

    return {"messages": AIMessage(content=confirmation_message), **extracted_model.model_dump()}