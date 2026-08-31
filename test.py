import pandas as pd

from main import(
clean_data,
clean_df,
make_dict_potential,
match_potential_to_similar_owned,
calculate_total_purchase_efficacy,
calculate_yearly_cpw,
print_recommendation

)


def test_make_dict_potential() -> None:
    print('Expected: ')
    print(f'Actual: ')


def test_match_potential_to_similar_owned() -> None:
    print()


def test_calculate_yearly_cpw() -> None:
    print()

def test_total_purchase_efficacy() -> None:


def test_print_recommendation() -> None:
    print()


def test_all():
    print()
    print('Testing all functions!')
    print('-----------------------')
    # insert test functions
    test_make_dict_potential()
    test_match_potential_to_similar_owned()
    test_calculate_yearly_cpw()
    test_total_purchase_efficacy()
    test_print_recommendation()
    print("-------- DONE! ---------")


if __name__ == "__main__":
    test_all()
