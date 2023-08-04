from googlesearch import search
import webbrowser

query = input("Please enter the phrase you want to search on Google: ")
number_of_searching = int(input(
    "Enter the number of sites you want to enter (do not enter too high numbers!): "))
print("Please wait...")

results = list(search(query, num_results=number_of_searching))

print("Results Found:")
for i, result in enumerate(results):
    print(f"{i+1}. {result}")

open_in_browser = input("Do you want to open the pages? (y/no): ")
if open_in_browser.lower() == "y":
    for result in results:
        webbrowser.open_new_tab(result)
else:
    with open("search_results.txt", "w") as f:
        for result in results:
            f.write(result + "\n")
    print("Search results saved in 'search_results.txt' file.")
