import json
from openai import OpenAI
from datasets import load_dataset


# System and user prompts
SYSTEM_MSG = """You are a financial analyst specializing in earnings call transcripts. You will receive the complete transcript of an earnings call, which includes both the prepared remarks and the Q&A session. Your job is to identify the key factors from the transcript and assign probabilities to the potential outcomes of these factors."""

USER_PREFIX = """Your task is to conduct a comprehensive analysis of the earnings call transcript below. Be sure to accurately capture the important factors and estimate the likelihood of each factor resulting in specific outcomes.\n\n"""

USER_TRANS_SUFFIX = """Please analyze the above earnings call transcript, focusing on the following key factors:
1. economic health: Economic health refers to the overall stability and performance of the economy, reflected in factors like growth, employment, inflation, and market confidence. Outcomes: {positive-outlook, unknown-or-uncertain}
2. market sentiment and investor psychology: Market sentiment reflects the overall mood or attitude of investors toward a particular market, influenced by news, economic data, and global events. Investor psychology refers to the emotions and cognitive biases that drive decisions, often leading to behaviors like fear-driven selling or greed-fueled buying. Outcomes: {optimistic, unknown-or-uncertain}
3. political events and government policies: Political events and government policies can significantly impact businesses and markets. This includes factors such as election outcomes, policy changes, and geopolitical tensions. Outcomes: {major upheaval, unknown-or-uncertain}
4. natural disasters and other 'black swan' events: Natural disasters and other "black swan" events can cause sudden and severe disruptions in financial markets, often leading to panic selling and increased volatility. Investor psychology during these events tends to be driven by fear and uncertainty, leading to irrational decisions and market overreactions. Outcomes: {major impact, unknown-or-uncertain}
5. geopolitical issues: Such as conflicts, trade disputes, or political instability, can disrupt financial markets by increasing uncertainty and affecting investor confidence. Outcomes: {escalation to conflict, unknown-or-uncertain}
6. merges and major acuisitions: Mergers and acquisitions involve the combining of two companies, where a merger is a mutual decision to join forces, while an acquisition is when one company takes over another. Outcomes: {positive-outlook, unknown-or-uncertain}
7. regulatory changes and legal issues happened: Regulatory changes often include stricter financial reporting requirements, compliance with corporate governance rules, and adherence to securities laws. Legal issues can involve insider trading, disclosure of material information, and adherence to environmental, social, and governance (ESG) standards. Outcomes: {positive-outlook, unknown-or-uncertain}
8. financial health: Financial health refers to the financial stability and performance of a company, reflected in factors like revenue growth, profitability, cash flow, and debt levels. Outcomes: {positive-outlook, unknown-or-uncertain}
9. company growth: A company growth focuses on sustainable expansion through consistent revenue increases, market share growth, and expansion into new markets or product lines. Outcomes: {positive-outlook, unknown-or-uncertain}
10. company product launches: Product launches refer to the introduction of new products or services by a company. Outcomes: {positive-outlook, unknown-or-uncertain}
11. supply chain: Supply chain refers to the network of businesses and organizations involved in the production, distribution, and delivery of goods and services. Outcomes: {positive-outlook, unknown-or-uncertain}
12. tech innovation: Tech innovation refers to the development and application of new technologies to improve products, services, or internal processes. Outcomes: {positive-outlook, unknown-or-uncertain}

Please take the time to thoroughly understand the transcript. For each key factor, provide a detailed summary based on the given transcript. Then, review all associated outcomes and assess the likelihood of each outcome. The likelihood should be strictly selected from the following options: {very likely, likely, somewhat likely, somewhat unlikely, unlikely, very unlikely}. Format your response in JSON.

# Example Output:
{
    "economic_health": {
        "summary": <Detailed summary of economic health mentioned in transcript>,
        "outcomes": {
            "positive-outlook": very likely,
            "unknown-or-uncertain": very unlikely
        }
    },
    ...
}

# Your Output:
"""

def call_openai_model(messages, api_key, model="gpt-4o-2024-08-06", max_tokens=8192):
    """
    Call OpenAI model with given messages
    
    Args:
        messages: List of message dictionaries with 'role' and 'content'
        api_key: OpenAI API key
        model: Model name to use
        max_tokens: Maximum tokens in response
    
    Returns:
        Parsed JSON response or None if error
    """
    client = OpenAI(api_key=api_key)
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=max_tokens,
            temperature=0.7,
            response_format={"type": "json_object"}
        )
        
        json_response = json.loads(response.choices[0].message.content)
        return json_response
    
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return None

def process_transcript(transcript, api_key):
    """
    Process earnings call transcript and return factor analysis
    
    Args:
        transcript: String containing the full transcript in JSON format
        api_key: OpenAI API key
    
    Returns:
        JSON object with factor analysis
    """
    # Parse transcript if it's a JSON string
    content = str(transcript)
    
    # Prepare messages for OpenAI
    messages = [
        {"role": "system", "content": SYSTEM_MSG},
        {"role": "user", "content": USER_PREFIX + content + "\n\n" + USER_TRANS_SUFFIX}
    ]
    
    # Call OpenAI model
    result = call_openai_model(messages, api_key)
    
    return result

def preprocess_trans(trans_section):
    section_content = ""
    for sec in trans_section:
        name = sec.get('name', 'Unknown')
        speech = " ".join(sec.get('speech', ''))
        section_content += f"{name}: {speech}\n"
    return section_content.strip()

def process_trans_list(trans_list, api_key, output_file="factor_profiles.json"):
    output = {}
    for transcript in trans_list:
        ect_id = transcript.get('ect_id', 'Unknown')
        if ect_id == 'Unknown':
            continue

        pp_remarks = preprocess_trans(transcript.get('prepared_remarks', []))
        qa_section = preprocess_trans(transcript.get('questions_and_answers', []))

        full_transcript = f"Earnings Call Transcript for {ect_id}\n\n# Prepared Remarks\n{pp_remarks}\n\n# Questions and Answers\n{qa_section}"

        # Call OpenAI to process the full transcript
        factor_profile = process_transcript(full_transcript, api_key)
        if factor_profile:
            output[ect_id] = factor_profile
        else:
            print(f"Failed to process transcript for {ect_id}")
    # Save output to JSON file
    with open(output_file, 'w') as f:
        json.dump(output, f, indent=4)
    return output

# Example usage
if __name__ == "__main__":
    # Example API key (replace with actual key)
    API_KEY = "your-openai-api-key-here"
    
    # Load dataset from Hugging Face
    print("Loading dataset from Hugging Face...")
    ect_transcripts_all = load_dataset("huuuyeah/DeFine", "data", split='ect_transcripts')
    print("Dataset loaded successfully.")
    # Process the transcripts
    process_trans_list(ect_transcripts_all, API_KEY, output_file="factor_profiles.json")