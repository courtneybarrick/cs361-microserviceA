import json


def main():
    # Read input.txt to get title of TV show
    with open('input.txt', 'r') as file:
        title = file.read().strip()

    # Load JSON
    filename = 'shows.json'
    with open(filename, 'r') as file:
        data = json.load(file)

    # Search JSON for given show title
    matched_show = None
    for show in data:
        if show.get('title').lower() == title.lower():
            matched_show = {
                'rating': show.get('rating'),
                'genre': show.get('genre'),
                'episode duration': show.get('episode duration')
            }
            break
        else:
            matched_show = None

    # Write result to output.txt
    with open('output.txt', 'w') as file:
        if matched_show:
            file.write(json.dumps(matched_show, indent=2))
        else:
            file.write(f"No show found with title '{title}'.")


if __name__ == '__main__':
    main()