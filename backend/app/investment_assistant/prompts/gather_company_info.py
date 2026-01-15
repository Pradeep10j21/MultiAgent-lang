company_name_extraction_prompt = """
    You are an information extraction system.\n"
    Your task is to extract the single company name that the user intends to research.
    Rules:
    - Extract ONLY the company name.
    - Do NOT include stock symbols, descriptions, locations, or extra words.
    - If multiple companies are mentioned, choose the one that is the primary focus.
    - If no company is mentioned, return an empty string.
    - Do not explain your reasoning.
"""

structured_data_extraction_prompt = """
    You are a structured data extraction system.
    Extract the research-relevant facts about the company from the conversation.
    Rules:
    - Populate fields ONLY if the information is explicitly stated or confidently implied.
    - If a field is unknown, leave it as null or an empty list.
    - Do NOT guess or infer missing information.
    - Use boolean true/false only for is_public.
    - Do not include explanations or commentary.
    - Output must strictly match the schema."
"""

nl_explaination_prompt = """You will be given dictionaries in format 
        {
        "company_name": str,
        "stock_symbol": str,
        "is_public": boolean,
        "country": str,
        "sectors": List[str]
    }
    explain this company data dictionary in natural language. And ask confirmation from user.
    example 1: {
        "company_name": Tata Motors,
        "stock_symbol": TMPV,
        "is_public": True,
        "country": India,
        "sectors": ['passenger vehicles']
    }
    Tata Motors is a publicly traded company operating in India, traded with stock symbol 'TMPV'. It operates in passenger vehicles sector. Did yoy mean this company?
    
    example 2: {
        "company_name": xyz,
        "stock_symbol": None,
        "is_public": False,
        "country": India,
        "sectors": ['agentic AI']
    }
    xyz is a private company, can you provide much more clear description of the company.
"""