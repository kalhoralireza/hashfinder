import hashlib
import argparse
from rich import print
from itertools import combinations_with_replacement

def print_banner():
    banner = r"""[white]
  _    _           _     ______ _           _           
 | |  | |         | |   |  ____(_)         | |          
 | |__| | __ _ ___| |__ | |__   _ _ __   __| | ___ _ __ 
 |  __  |/ _` / __| '_ \|  __| | | '_ \ / _` |/ _ \ '__|
 | |  | | (_| \__ \ | | | |    | | | | | (_| |  __/ |   
 |_|  |_|\__,_|___/_| |_|_|    |_|_| |_|\__,_|\___|_|   
    [/white]                               
    [bold][green]Blog: https://alirezakalhor.blogspot.com/[/green]
    [green]Github: https://github.com/kalhoralireza/[/green][/bold]
"""
    print(banner)

def calculate_hashes(combination: list, splitter: str) -> dict:
    """Calculate hashes for a given combination of texts using all available hash algorithms.

    Args:
        combination (list): List of text strings.
        splitter (str): The splitter character used to join the text strings.

    Returns:
        dict: Dictionary of hash algorithms and their corresponding hash values.
    """
    hash_algorithms = hashlib.algorithms_available
    hashes = {}
    
    for algo in hash_algorithms:
        if algo.startswith('shake_'):
            continue
        hash_function = hashlib.new(algo)
        text = splitter.join(combination)
        hash_function.update(text.encode('utf-8'))
        hashes[algo] = hash_function.hexdigest()
    
    return hashes


def generate_combinations(items: list) -> list:
    """Generate all combinations with replacement of the provided items.

    Args:
        items (list): List of items to generate combinations.

    Returns:
        list: List of combinations.
    """
    results = []
    for comb in combinations_with_replacement(items, len(items)):
        if list(comb) not in results:
            results.append(list(comb))
    return results


def find_probable_values(text_combinations: list, splitters: list, target_hash: str, combine_splitters: bool):
    """Find probable values by comparing generated hashes with the target hash.

    Args:
        text_combinations (list): List of text combinations.
        splitters (list): List of splitter characters.
        target_hash (str): The target hash to compare against.
        combine_splitters (bool): Whether to combine splitters or not.
    """

    if combine_splitters:
        splitter_combinations = generate_combinations(splitters)
    else:
        splitter_combinations = splitters

    for combination in text_combinations:
        for split_combo in splitter_combinations:
            #splitter = ''.join(split_combo) if combine_splitters else split_combo[0]
            splitter = ''.join(split_combo)
            hashes = calculate_hashes(combination, splitter)
            for alg, hash_value in hashes.items():
                if target_hash in hash_value:
                    print(f"[green][*] Match found:\n\t [green]{splitter.join(combination)} : {hash_value} : {alg}[/green]")
                    return
    print("[red][!] No matches found.[/red]")

def print_hashes(text_combinations: list, splitters: list, combine_splitters: bool):
    """Print all hash values of given texts.

    Args:
        text_combinations (list): List of text combinations.
        splitters (list): List of splitter characters.
        combine_splitters (bool): Whether to combine splitters or not.
    """
    if combine_splitters:
        splitter_combinations = generate_combinations(splitters)
    else:
        splitter_combinations = splitters

    for combination in text_combinations:
        for split_combo in splitter_combinations:
            #splitter = ''.join(split_combo) if combine_splitters else split_combo[0]
            splitter = ''.join(split_combo)
            hashes = calculate_hashes(combination, splitter)
            print(f"[bold]{splitter.join(combination)}[/bold]")
            for alg, hash_value in hashes.items():
                print(f"    [blue]{alg}[/blue]:[green]{hash_value}[/green]")
                    
def main():

    parser = argparse.ArgumentParser(description="Calculate all possible hashes for a given text combinations. Use it for finding weak tokens!")
    parser.add_argument("--text", type=str, help="Comma-separated list of texts to hash.", required=True)
    parser.add_argument("--hash", type=str, help="Target hash to compare generated hashes with.", required=False)
    parser.add_argument("--splitter", type=str, help="Comma-separated list of splitters. Default: '|, &, <space>, <,>, <concatination>")
    parser.add_argument("--combine", help="Combine splitters.", action="store_true")
    parser.add_argument("--print", help="Print all possible hashes for a given text combinations to terminal.", action="store_true")
    parser.add_argument("--silent", help="Do not print the banner.", action="store_true", default=False)
    args = parser.parse_args()

    if not args.silent:
        print_banner()
    
    texts = [text.strip() for text in args.text.split(',')]
    if not args.splitter:
        splitters = ["-", ":", "|", "&", ",", " ", ""]
    else:
        splitters = [splitter.strip() for splitter in args.splitter.split(',')]
        print(f"[white][*] Using provided splitters:[/white] {splitters}")
    text_combinations = generate_combinations(texts)

    
    if args.print:
        print_hashes(text_combinations, splitters, args.combine)
    else:
        if not args.hash:
            print("[yellow][!][/yellow] Please provide the target hash for comparision.")
        else: 
            find_probable_values(text_combinations, splitters, args.hash, args.combine)


if __name__ == "__main__":
    main()
