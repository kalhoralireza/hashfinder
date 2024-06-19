# Hashfinder

This Python script generates all possible combinations of given texts, applies various hash functions to these combinations, and compares the resulting hashes with a target hash. The script is highly customizable with options for different splitters and combinations of splitters.

## Features

- Generates combinations with replacement of the provided texts.
- Applies all available hash algorithms (excluding shake algorithms).
- Compares generated hashes with a target hash to find probable values.
- Supports custom splitters and combinations of splitters.

## Requirements

- Python 3.x
- Python rich mdule

## Installation

1. Clone the repository.
2. Navigate to the project directory.
3. Install dependencies.
4. Ready to use!
```bash
git clone https://github.com/kalhoralireza/hashfinder.git
cd ./hashfinder
pip3 install -r ./requirements
```
## Usage
Run the script with the following command:
```bash
python hashfinder.py --text "text1,text2,text3" --hash "target_hash" [--splitter "splitter1,splitter2"] [--combine-splitters] [--print]
```
### Arguments
- `--text`: Comma-separated list of texts to hash. (Required)
- `--hash`: Target hash to compare generated hashes with. (Required if not using `--print`)
- `--splitter`: Comma-separated list of splitters. Default: `-`, `:`, `|`, `&`, `,`, `<space>`, `<concationation>` (Optional)
- `--combine-splitters`: Combine splitters. (Optional)
- `--print`: Outputs the generates hashes to the terminal.

## Examples
Calculate hashes for given texts with default splitters:
```bash
python3 hashfinder.py --text "apple,banana,cherry" --hash "61ed72632b351843c1ea6f4148860589ea7eeea30fb6d082336476f7d231e774"
```
Calculate hashes for given texts with custom splitters:
```bash
python3 hashfinder.py --text "apple,banana,cherry" --hash "61ed72632b351843c1ea6f4148860589ea7eeea30fb6d082336476f7d231e774" --splitter "|,-,:"
```
Combine splitters:
```bash
python3 hashfinder.py --text "apple,banana,cherry" --combine --splitter "|,:" --hash "cdb7b7655e50ab1bcb5a59b460b039a46e75d5b2ed4aafecd8d3f62151ce2f371c0380cf5f9986f70699310e5b14a128b7e5ee091a6db29c5128667b9f59c77f"
```
## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any bugs, improvements, or features.

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/kalhoralireza/hashfinder/blob/main/LICENSE) file for details.