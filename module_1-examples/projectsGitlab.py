import requests
import operator

def main():
   gitlab_user = "whyorean"
   gitlab_api_url = "https://gitlab.com/api/v4/"

   projects_endpoint = f"users/{gitlab_user}/projects"
   response = requests.get(gitlab_api_url + projects_endpoint)
   # print(response)
   # print(response.text)
   # print(response.json())

   projects = response.json() # type of projects?
   sorted_projects = sorted(projects, key=operator.itemgetter("last_activity_at"), reverse=True)
   result = [(project["name"], project["last_activity_at"]) for project in sorted_projects]
   print("\n".join(map(str, result)))

if __name__ == '__main__':
    main()