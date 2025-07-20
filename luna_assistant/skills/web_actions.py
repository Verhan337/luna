from duckduckgo_search import ddg

def handle(intent, entities):
    if intent == "web_search":
        query = entities.get("query")
        if not query:
            return "No search query provided."
        try:
            results = ddg(query, max_results=1)
            if results:
                return f"Top result: {results[0]['title']} - {results[0]['href']}"
            else:
                return "No results found."
        except Exception as e:
            return f"Error searching the web: {e}"
    return "Unknown web action."