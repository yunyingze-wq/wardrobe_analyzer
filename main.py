
"""pcode
MVP:
1. calcluate projecteed cost per wear based on user habits
2. give the best recommendation

"""
import pandas as pd

# next step: get ur csv, edit it a bit, read it here


def clean_data(col: str) -> str:
    # strip potential symbols from user's inputs from excel
    cleaned = str(col).strip(' $').lower()
    return cleaned


def clean_df(wardrobe_df: pd.DataFrame) -> pd.DataFrame:
    clean = wardrobe_df.copy()
    # prevent crashes:
    # not affected by excel dropdown rules
    clean = clean.fillna('n/a')
    for col in clean:
        clean[col] = clean[col].apply(clean_data)
    return clean

#def make_input_df(category: pd.Series, price: pd.Series, occasions: pd.Series) -> pd.DataFrame:
    # constructs a df based on user inputs
    # for MVP, we only pick the main category and occasion
    # since all are pd.series, how do we type cast to float vs str?
def make_dict_potential(category: str, price: float, occasions: str) -> dict[str, str | float]:
    # if you do inpputs in helper directly, ur helper takes nothing and thats the antithesis of a function
    # take inputs in main, only construct dict
    # backlog: you could take a series for eact variable in V2 for mutiple occasions tag
    return {
        'category': category,
        'price': price,
        'occasions': occasions
    }

# this is not needed i think
def categorize_potential_piece() -> pd.Series:
    # prompt user to fill out a few critical labels (category, price, occasions)
    # Question: should this printing happen here or main? i think main
    print('To help you decide, I need a couple of details')
    print('')
    # piece_info is not a str. we need to construct a DF before we call clean_df on it.
    make_dict_potential()
    clean_df(piece_info)
    return 0


def match_potential_to_similar_owned(
        owned_df: pd.DataFrame, maybe_buy: dict[str, str | float]
        ) -> list[Any]:
    # returns a list of three most similar items and their usage scores
    # handle the interesting problem of 4 basic tees having a higher score than
    # 1 additional babydoll top
    # this should not only compare use history to the respective dilemma piece,
    # now its wears_per_year
    if
    return []


def calculate_average_use_per_item(dilemma_piece: str) -> float:
    # divide by the 'quantity' to get per item results
    # takes labels: quantity, category, occasions, price, weekly_wears (1 item)
    # it should also generate insights for yearly use (we display in the explanation)
    # this solves the problem of basics in higher quantity but higher in usage than an occasial item

    score = dilemma_piece
    return 0

# optional: calc reduandancy score


def calculate_cost_per_wear() -> float:
    return 0


def calculate_total_purchase_efficacy() -> pd.DataFrame:
    # this could be a menu-equse layout of your items and cost-per-use, or it
    # can be more like total efficacy of an order and highlight the bad choices
    # choose the easiest on MVP
    return pd.DataFrame()


def print_recommendation_results() -> str:
    # this prints info like cost_per_wear (CPW) along with items, highlights
    # bad usage items, and tells user about the CPW of a particular bad item
    return ''


def main() -> None:
    # make this pretty later
    print()
    print('----------------------------------------------')
    print('Welcome to your virtual shopping bestie!/n')
    print('----------------------------------------------')
    user_excel = input(
        " Please enter the name of your Excel file with .xlsx: /n ex: " \
        "my_clothes.xlsx"
                       )
    # for testing:yunying_wardrobe_tester.xlsx
    user_wardrobe = pd.read_excel(user_excel)
    potential_buy = input('Enter the piece you want to buy: ')
    category = input(
        'Enter what category of clothing your piece is:/n (Top,Sweater' \
        'Outerwear,Pants,Shorts,Skirt Dress,Activewear) '
        )
    price = input('Enter the price of your item ')
    occasions = input(
        'Enter the main occasion you anticipate wearing this for '
        )
    make_dict_potential(category, float(price), occasions)
    # call make_df to make a comparision df of the potential_buy to user_wardrobe
    # functions use this variable
    # Todo: call all functions
    # make a decision variable to store your decision and to print that
    print()
    print("Enjoy your new fits!")


if __name__ == '__main__':
    main()
