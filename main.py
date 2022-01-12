import re
import time

import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

MAX_WAIT = 10
WEBSITE = "https://en.wikipedia.org/wiki/SQL"


def open_website(website: str) -> list[str]:
    """Launches a browser session with the given URL, find the necessary
    tables, returns a list of dictionaries with table content and closes
    the browser session."""
    driver = webdriver.Firefox()
    driver.get(website)
    tables = find_table_elements(driver)
    extracted_tables = retrieve_table_data_from_elements(tables)
    driver.quit()
    return extracted_tables


def find_table_elements(driver: webdriver.Firefox) -> list[WebElement]:
    """Returns a list of all elements of class 'wikitable'"""
    start_time = time.time()
    try:
        tables = driver.find_elements(By.CLASS_NAME, "wikitable")
    except (AssertionError, WebDriverException) as e:
        if time.time() - start_time > MAX_WAIT:
            print("Unable to find element, ending script")
            raise e
        time.sleep(0.5)
    return tables


def retrieve_table_data_from_elements(tables) -> list[dict[int : dict[int:str]]]:
    """Builds a list of dictionaries for each element of class wikitable.
    The dictionaries have the following structure:
    { 0 : { 0 : "first column title", 1 : "second column title", 2 : "third column title"},
      1 : { 0 : "first row/first col data", 1: "first row/second col data", 2 : "first row/third col data" },
      2 : { 0 : "second row/first col data", 2 : "second row/second col data", 3 : "second row/third col data"},
      etc.
    }"""
    start_time = time.time()
    table_list = []
    for table in tables:
        try:
            results = {}
            rows = table.find_elements(By.TAG_NAME, "tr")
            thead = rows[0].find_elements(By.TAG_NAME, "th")
            results[0] = {cnt: col.text for cnt, col in enumerate(thead)}
            for count, row in enumerate(rows[1:]):
                count += 1
                columns = row.find_elements(By.TAG_NAME, "td")
                results[count] = {cnt: col.text for cnt, col in enumerate(columns)}
            table_list.append(results)
        except (AssertionError, WebDriverException) as e:
            if time.time() - start_time > MAX_WAIT:
                print("Unable to find element, ending script")
                raise e
        time.sleep(0.5)
    return table_list


def clean_up_results(dictionary: dict[int : dict[int:str]]) -> pd.DataFrame:
    """Takes a nested dictionary as input and returns a pandas dataframe with
    cleaned up results"""
    df = pd.DataFrame.from_dict(dictionary, orient="index")
    try:
        # Remove any text between brackets (i.e. links or 'citations needed')
        df = df.applymap(lambda x: re.sub("\[.*?\]", "", x))
        # Remove any * or † characters
        df = df.applymap(lambda x: re.sub("[†\*].*?", "", x))
    except TypeError:
        # If the regexes had no result, it'll throw a type error.
        # We can ignore the type error as it means nothing was found that needed
        # to be replaced.
        pass
    # promote headers
    df.columns = df.iloc[0]
    df = df.drop(0, axis=0)
    return df


def main():
    table_list = open_website(WEBSITE)
    dfs = [clean_up_results(table) for table in table_list]
    for count, df in enumerate(dfs, start=1):
        df.to_csv(f"output_{count}.csv", index=False)
    print(f"Copied {len(dfs)} table(s) from {WEBSITE} to 'output_#.csv' file(s)")


if __name__ == "__main__":
    main()
