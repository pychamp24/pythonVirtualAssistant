import wolframalpha

wolfram_app_id = "8R2P5P-G6484VQWTP" 
client = wolframalpha.Client(wolfram_app_id)

def calculate_query(query):
    try:
        response = client.query(query)
        
        answer = next(response.results).text
        return answer
    except Exception as e:
        return "I'm sorry, I couldn't process the query."

