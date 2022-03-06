interface AlphabetFilterProps {
    availableLetters?: string[];
    selectedLetter?: string;
    onSelectLetter(letter: string): void;
}

export default function AlphabetFilter({ availableLetters = [], selectedLetter, onSelectLetter }: AlphabetFilterProps) {
    const alphabet = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ];

    return (
        // TODO: fixt style (first couple of letters and last couple of letters are hidden)
        <div className="alphabet">
            <ul className="alphabet__navigation">
                {alphabet.map((letter) => {
                    let className = "alphabet__button";
                    if (letter === selectedLetter) {
                        className += " alphabet__button--active";
                    }
                    if (!availableLetters.includes(letter)) {
                        className += " alphabet__button--disabled";
                    }

                    return (
                        <li className="alphabet__list" key={letter} onClick={() => onSelectLetter(letter)}>
                            <div className={className}>{letter}</div>
                        </li>
                    );
                })}
            </ul>
        </div>
    );
}
