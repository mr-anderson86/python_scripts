# Script searches Nasa website for all Ilan Ramon's images and videos
# and prints only those who are larger than 1000 KB.
# Also it outputs all to CSV file (in project main directory)

import csv, json, os, warnings, requests
import utilities.log_utility as utilities

warnings.filterwarnings("ignore")
#os.environ['http_proxy'] = 'http://genproxy:8080'  # if needed, uncomment this line
#os.environ['https_proxy'] = 'https://genproxy:8080'  # if needed, uncomment this line
logger = utilities.setup_custom_logger(__name__)


def validate_parameters(object_to_search, media_type, year_start, year_end):
    parameters_dict = {
        "object_to_search": None,
        "media_type": None,
        "year_search": None
    }

    if object_to_search:
        object_to_search = object_to_search.replace(" ", "%20")
        parameters_dict["object_to_search"] = object_to_search
    else:
        return False, "missing object_to_search", None
    if media_type:
        media_type = media_type.replace(" ", ",")
    else:
        media_type = "image,video"
    parameters_dict["media_type"] = media_type
    if year_start and year_end and year_start.isdigit() and year_end.isdigit():
        parameters_dict["year_search"] = "&year_start=" + year_start + "&year_end=" + year_end

    return True, None, parameters_dict


def get_json(parameters_dict):
    logger.info("going to send api request to nasa api")
    url = "https://images-api.nasa.gov/search?q=" + parameters_dict["object_to_search"] + "&media_type=" + \
          parameters_dict['media_type'] + (parameters_dict['year_search'] if parameters_dict['year_search'] else "")
    logger.info("url = " + url)
    try:
        response = requests.get(url)
        data = json.loads(response.text)
        return True, None, data
    except Exception as e:
        return False, "failed to load json. error details: " + str(e.message), None


def print_items(json_data, object_to_search):
    # print json.dumps(json_data, indent=1)
    obj = object_to_search.replace(" ", "_")
    
    with open(obj + '.csv', 'wb') as csvfile:
        fieldnames = ['Nasa_id', 'Size']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        print "Nasa_id, Size"

        items = json_data['collection']['items']
        # iterating through all items, retrieving its metadata, and from there getting size.
        for item in items:
            url = item['href']
            try:
                response = requests.get(url)
                data = json.loads(response.text)
                # print json.dumps(data, indent=1)

                metadata_url = data[len(data) - 1]
                response = requests.get(metadata_url)
                data = json.loads(response.text)
                # print json.dumps(data, indent=1)

                nasa_id = data['AVAIL:NASAID']
                image_size = data['File:FileSize']
                image_size_num = float(image_size.split(' ', 1)[0])
                image_size_type = str(image_size.split(' ', 1)[1])

                if (image_size_type.lower() == 'kb' and image_size_num > 1000) or (
                                image_size_type.lower() == 'mb' and image_size_num > 0.9765625):
                    writer.writerow({'Nasa_id': str(nasa_id), 'Size': str(image_size_num) + " " + str(image_size_type)})
                    print(str(nasa_id) + "," + str(image_size_num) + " " + str(image_size_type))
            except Exception as e:
                print "couldn't print item: " + str(e.message)
                exit(1)


if __name__ == '__main__':
    search_item = "Ilan Ramon"
    is_executed, msg, parameters_dict = validate_parameters(search_item, None, None, None)
    if is_executed:
        is_executed, msg, json_data = get_json(parameters_dict)
        if is_executed:
            print_items(json_data, search_item)
        else:
            logger.error(msg)
    else:
        logger.error(msg)
