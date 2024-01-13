import wikipedia

while True:
    # Prompt the user for a page title or search phrase
    query = input("Enter a Wikipedia page title or search phrase (press Enter to quit): ")

    # If the user enters blank input, exit the loop
    if not query:
        break

    try:
        # Try to get a Wikipedia page with the given query
        # Customize how the page is determined to avoid unexpected results
        page = wikipedia.page(query, auto_suggest=False)

        # Print the page title, summary, and URL
        print(f"Title: {page.title}")
        print(f"Summary: {page.summary}")
        print(f"URL: {page.url}")

    except wikipedia.exceptions.DisambiguationError as e:
        # Handle disambiguation page exception by printing options
        print("Disambiguation page found. Options:")
        for option in e.options:
            print(option)

    except wikipedia.exceptions.PageError:
        # Handle page not found exception
        print("Page not found.")
