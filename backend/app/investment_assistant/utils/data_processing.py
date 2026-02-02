from langchain.messages import HumanMessage, AIMessage, AnyMessage
from typing import List


def swap_message_roles(messages: List[AnyMessage]):
    """
    Utility function to swap HumanMessage and AIMessage roles in a list of messages
    Used in conversation between AI Agents
    """
    for i in range(len(messages)):
        if isinstance(messages[i], AIMessage):
            messages[i] = HumanMessage(content=messages[i].content)
        elif isinstance(messages[i], HumanMessage):
            messages[i] = AIMessage(content=messages[i].content)
    
    return messages


def format_wikipedia_documents(search_docs):
    """ Format wikipedia documents into string """
    return "\n\n---\n\n".join(
        [
            f'<Document source="{doc.metadata["source"]}" page="{doc.metadata.get("page", "")}"/>\n{doc.page_content}\n</Document>'
            for doc in search_docs
        ]
    )

def format_web_search_documents(search_docs):
    """ Format web search documents into string """
    return "\n\n---\n\n".join(
        [
            f'<Document href="{doc["url"]}"/>\n{doc["content"]}\n</Document>'
            for doc in search_docs
        ]
    )
