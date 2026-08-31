
import pandas as pd
"""
MVP:
1. calcluate projecteed cost per wear based on user habits
2. give the best recommendation

"""


def clean_data(col: str) -> str:
    # strip potential symbols from user's inputs from their excel data
    cleaned = str(col).strip(' $').lower()
    return cleaned


def clean_df(wardrobe_df: pd.DataFrame) -> pd.DataFrame:
    clean = wardrobe_df.copy()
    # prevent crashes:
    clean = clean.fillna('n/a')
    for col in clean:
        clean[col] = clean[col].apply(clean_data)
    return clean


def make_dict_potential(name: str, category: str, price: float, occasions: str) -> dict[str, str | float]:
    # backlog: you could take a series for eact variable in V2 for mutiple occasions tag
    return {
        'name': name,
        'category': category,
        'price': price,
        'occasions': occasions
    }


def match_potential_to_similar_owned(
        wardrobe: pd.DataFrame, maybe_buy: dict[str, str | float]
        ) -> pd.DataFrame:
    # scoring: 4 basic tees have a higher score than 1 additional babydoll top
    mask = (
        (wardrobe["category"] == maybe_buy["category"])
        & (wardrobe["occasions"] == maybe_buy["occasions"])
    )
    same_df = wardrobe.loc[mask]
    # checks if "potential buy" is a unique item or not for user's closet
    if same_df.empty:
        return same_df
    # the top 3 is the ones closest in price and use scores
    same_df['price_diff'] = (same_df['price'] - maybe_buy['price']).abs()
    # returns the top three most similar items based on price, category, occasion
    return same_df.nsmallest(3, "price_diff")
    # backlog: calc reduandancy score


def calculate_yearly_cpw(wardrobe: pd.DataFrame) -> pd.DataFrame:
    # cpw is the cost per wear of an item
    # calculates this per item
    return round((wardrobe['price'] / wardrobe['wears_per_year']), 2)


def calculate_purchase_cpw(rank: pd.DataFrame) -> pd.DataFrame:
    # can be more like total efficacy of an order and highlight the bad choice
    rank['yearly_cpw'] = calculate_yearly_cpw(rank)
    sort_df = rank.sort_values('yearly_cpw', ascending=True)
    return sort_df


def calculate_marginal_value(similar_df: pd.DataFrame) -> float | None:
    # calculate average MV of owned similar items
    if similar_df.empty:
        return None
    return (similar_df['wears_per_year'].sum()) / (similar_df['quantity'].sum())

# Todo: calc_score()
# implememnt in V2: def wardrobe_wrapped(wardrobe: pd.DataFrame) -> None:
def make_decision(similar: pd.DataFrame, mv: float, cpw: float) -> str:
    if similar.empty:
        return 'I do not have any data on this item'
    owned_mv = calculate_marginal_value(similar)
    owned_cpw = calculate_purchase_cpw(similar).sum
    # TODO: past session: the probelm is that owned_mv is the value of another item
    # this means we should not have mv but rather look at ownedmv alone
    # get iloc of the 3 most similar item,
    avg_cpw = owned_cpw / 
    return decision


def print_recommendation(potential: str, wardrobe: pd.DataFrame) -> None:
    # this prints info like cost_per_wear (CPW) along with items, highlights
    # bad usage items, and tells user about the CPW of a particular bad item
    # prints the explanation chunk of the menu from main
    print(f'The average cost per wear of {potential} is {calculate_total_purchase_efficacy(wardrobe)}')
    print(f'I would {decision} based on these reasons: {}')


def main() -> None:
    print()
    print("=" * 54)
    print("               SHOULD I BUY THIS?")
    print("          your virtual shopping bestie")
    print("=" * 54)
    print("\nFirst, let's load your closet.\n")
    user_excel = input(
        "Enter your wardrobe Excel filename (.xlsx)\n"
        "Example: my_clothes.xlsx\n"
        "> "
    ).strip()
    # check that the user file is uploaded successfully
    try:
        user_wardrobe = pd.read_excel(user_excel)
        user_df = user_wardrobe.copy()
    except FileNotFoundError:
        print(f'Your file {user_excel} does not exist. Please try again')
    print("\n✓ Closet loaded.")
    print("Now tell me about the piece you're eyeing.\n")
    potential_buy = input(
        "What are you thinking about buying?\n"
        "> "
    ).strip()
    category = input(
        "\nCategory\n"
        "(Top, Sweater, Outerwear, Pants, Shorts, Skirt, "
        "Dress, Activewear)\n"
        "> "
    ).strip()
    price = float(
        input(
            "\nPrice ($)\n"
            "> "
        )
    )
    occasions = input(
        "\nWhat is the main occasion you'd wear it for?\n"
        "> "
    ).strip()
    maybe_buy = make_dict_potential(potential_buy, category, price, occasions)
    print("\n" + "-" * 54)
    print("                    THE DILEMMA")
    print("-" * 54)
    print(f"\nPiece:    {potential_buy}")
    print(f"Category: {category}")
    print(f"Price:    ${price:.2f}")
    print(f"Occasion: {occasions}")
    print("\nChecking this against what you actually wear...")
    # TODO:
    similar_items = match_potential_to_similar_owned(
         user_df,
         maybe_buy
    )
    # note: calc_marginal_v() can reeturn None! this should be explained in main
    decision, reason = make_decision()
    #     user_wardrobe,
    #     maybe_buy,
    #     similar_items
    # )
    #
    # print_recommendation(
    #     potential_buy,
    #     maybe_buy,
    #     similar_items,
    #     decision,
    #     reason
    # )
    print("\n" + "-" * 54)
    print("Your closet has receipts.")
    print("-" * 54)


if __name__ == '__main__':
    main()
