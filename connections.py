import pandas as pd
import random
import streamlit as st

# Manually define the word data and categories (instead of CSV)
def get_manual_data():
    # Example data in the form of a list of dictionaries, where each dictionary is a row.
    data = [
        ["Earthworm", "Eel", "Salamander", "Slug", "SLIMY ANIMALS"],
        ["Aurora", "Firefly", "Glowstick", "Radium", "THINGS THAT LUMINESCENCE"],
        ["Canal", "Clog", "Tulip", "Windmill", "DUTCH SYMBOLS"],
        ["Gatecrash", "Raindrop", "Skydive", "Waterfall", "ENDING WITH SYNONYMS FOR 'PLUNGE'"],
        ["Clips", "Eraser", "Pens", "Tapes", "THINGS FOUND IN A DESK DRAWER"],
        ["Breast", "Drumstick", "Thigh", "Wing", "PARTS OF A CHICKEN"],
        ["Card", "Five", "Note", "Tea", "WORDS THAT CAN FOLLOW 'HIGH'"],
        ["Bee", "Crow", "Dove", "Elf", "STARTS WITH A LETTER THAT LOOKS LIKE PART OF THE NEXT LETTER"],
        ["Bass", "Flute", "Oboe", "Trumpet", "ORCHESTRA INSTRUMENTS"],
        ["Cheer", "Delight", "Elation", "Joy", "SYNONYMS FOR HAPPINESS"],
        ["Clover", "Diamond", "Heart", "Spade", "SUIT SYMBOLS"],
        ["Cream", "Egg", "Milk", "Sugar", "BAKERY INGREDIENTS"],
        ["Bean", "Corn", "Pea", "Wheat", "TYPES OF GRAINS/SEEDS"],
        ["Brisk", "Crisp", "Sharp", "Snappy", "SYNONYMS FOR LIVELY"],
        ["Flip", "Jump", "Leap", "Vault", "VERBS FOR SUDDEN UPWARD MOVEMENT"],
        ["Glove", "Hat", "Scarf", "Shoes", "WINTER ACCESSORIES"],
        ["Blanket", "Curtain", "Pillow", "Sheet", "BEDDING ITEMS"],
        ["Brass", "Nickel", "Silver", "Steel", "TYPES OF METAL"],
        ["Catch", "Grab", "Seize", "Snatch", "VERBS FOR GRABBING QUICKLY"],
        ["Comet", "Meteor", "Planet", "Star", "THINGS FOUND IN SPACE"],
        ["Belt", "Bracelet", "Necklace", "Ring", "JEWELRY ITEMS"],
        ["Chalk", "Crayon", "Marker", "Paint", "ART SUPPLIES"],
        ["Couch", "Desk", "Lamp", "Table", "PIECES OF FURNITURE"],
        ["Frown", "Grin", "Scowl", "Smile", "FACIAL EXPRESSIONS"],
        ["Button", "Cuff", "Hem", "Seam", "PARTS OF A SHIRT"],
        ["Cheese", "Cracker", "Grapes", "Wine", "GO WELL WITH WINE"],
        ["Draft", "Leak", "Vent", "Wind", "THINGS THAT CAN ESCAPE"],
        ["Irony", "Sarcasm", "Satire", "Wit", "FORMS OF WORDPLAY"],
        ["Ankle", "Elbow", "Knee", "Wrist", "BODY JOINTS"],
        ["Cabin", "Hut", "Shack", "Tent", "SMALL SHELTERS"],
        ["Drum", "Guitar", "Piano", "Violin", "MUSICAL INSTRUMENTS"],
        ["Fog", "Haze", "Mist", "Smog", "TYPES OF THICK AIR"],
        ["Bowl", "Cup", "Plate", "Saucer", "TABLEWARE"],
        ["Chip", "Dip", "Salsa", "Tortilla", "THINGS YOU EAT WITH TORTILLA CHIPS"],
        ["Clock", "Dial", "Hand", "Number", "PARTS OF A CLOCK"],
        ["Float", "Glide", "Soar", "Drift", "VERBS FOR MOVING SMOOTHLY THROUGH AIR OR WATER"],
        ["Bread", "Butter", "Jam", "Toast", "BREAKFAST STAPLES"],
        ["Chain", "Link", "Ring", "Shackle", "THINGS MADE OF CONNECTED PIECES"],
        ["Earth", "Fire", "Water", "Wind", "THE CLASSIC FOUR ELEMENTS"],
        ["Hose", "Nozzle", "Sprinkler", "Valve", "GARDENING TOOLS/SUPPLIES"],
        ["Bass", "Tiger", "Zebra", "Zucchini", "THINGS WITH STRIPES"],
        ["Cage", "Habitat", "Zoo", "Wild", "PLACES TO SEE WILD ANIMALS"],
        ["Burst", "Erupt", "Spew", "Surge", "WORDS RELATED TO SUDDEN MOVEMENT"],
        ["Bear", "Fare", "Pair", "Stare", "RHYMES WITH 'HAIR'"],
        ["Chalkboard", "Desk", "Globe", "Map", "THINGS FOUND IN A CLASSROOM"],
        ["Ballet", "Jazz", "Salsa", "Tap", "TYPES OF DANCES"],
        ["Charm", "Spell", "Trick", "Wand", "WORDS ASSOCIATED WITH MAGIC"],
        ["Knife", "Needle", "Razor", "Thorn", "THINGS THAT ARE SHARP"],
        ["Ball", "Coin", "Orbit", "Wheel", "THINGS THAT ARE ROUND"],
        ["Author", "Novel", "Plot", "Verse", "WORDS RELATED TO WRITING"],
        ["Carrot", "Lettuce", "Radish", "Tomato", "THINGS YOU MIGHT FIND IN A SALAD"],
        ["Add", "Bee", "Hill", "Jazz", "END IN DOUBLE LETTERS"],
        ["Blue", "Green", "Orange", "Violet", "COLORS IN A RAINBOW"],
        ["Computer", "Lamp", "Phone", "Toaster", "THINGS YOU PLUG IN"],
        ["Climax", "Denouement", "Epilogue", "Finale", "WORDS RELATED TO A STORY'S ENDING"],
        ["Box", "Fox", "Lynx", "Taxi", "CONTAIN THE LETTER 'X'"],
        ["Boots", "Sneakers", "Socks", "Sandals", "THINGS YOU WEAR ON YOUR FEET"],
        ["Foot", "Gallon", "Pound", "Yard", "WORDS RELATED TO MEASUREMENT"],
        ["Cloud", "Moon", "Rain", "Sun", "THINGS FOUND IN THE SKY"],
        ["Ash", "Fir", "Oak", "Pine", "START WITH A TYPE OF TREE"],
        ["Coffee", "Grapefruit", "Hops", "Rhubarb", "THINGS THAT CAN BE BITTER"],
        ["Board", "Dice", "Piece", "Token", "WORDS RELATED TO A GAME"],
        ["Dish", "Faucet", "Sponge", "Strainer", "THINGS YOU FIND IN A KITCHEN SINK"],
        ["Aloe", "Blue", "Echo", "Idea", "END IN A VOWEL"],
        ["Bottle", "Jar", "Pail", "Tub", "TYPES OF CONTAINERS"],
        ["Echo", "Noise", "Rhythm", "Tune", "WORDS RELATED TO SOUND"],
        ["Clown", "Lion", "Tent", "Trapeze", "THINGS YOU SEE AT A CIRCUS"],
        ["Do", "Fa", "La", "Ti", "START WITH A MUSICAL NOTE"],
        ["Beet", "Daisy", "Mint", "Peony", "THINGS THAT GROW IN A GARDEN"],
        ["Dash", "Haste", "Pace", "Swift", "WORDS RELATED TO SPEED"],
        ["Brush", "Mirror", "Soap", "Towel", "THINGS YOU FIND IN A BATHROOM"],
        ["IQ", "Iraq", "Qatar", "Squawk", "CONTAIN THE LETTER 'Q'"],
        ["Ice", "Snow", "Winter", "Wind", "THINGS THAT ARE COLD"],
        ["Dread", "Fright", "Panic", "Terror", "WORDS RELATED TO FEAR"],
        ["Axe", "Knife", "Scissors", "Shears", "THINGS YOU USE TO CUT"],
        ["Baker", "Driver", "Farmer", "Teacher", "END IN 'ER'"],
        ["Candy", "Honey", "Sugar", "Syrup", "THINGS THAT ARE SWEET"],
        ["Flight", "Journey", "Trip", "Voyage", "WORDS RELATED TO TRAVEL"],
        ["Book", "Card", "Shelf", "Stack", "THINGS YOU FIND IN A LIBRARY"],
        ["Blue", "Gold", "Gray", "Red", "START WITH A COLOR"],
        ["Bag", "Cup", "Door", "Umbrella", "THINGS WITH A HANDLE"],
        ["Big", "Huge", "Little", "Tiny", "WORDS RELATED TO SIZE"],
        ["Deer", "Leaf", "Moss", "Tree", "THINGS YOU FIND IN A FOREST"],
        ["Baking", "Drawing", "Singing", "Writing", "END IN 'ING'"],
        ["Cloud", "Cotton", "Feather", "Velvet", "THINGS THAT ARE SOFT"],
        ["Gaze", "Glance", "Look", "Stare", "WORDS RELATED TO SEEING"],
        ["Car", "Gas", "Oil", "Tire", "THINGS YOU FIND IN A GARAGE"],
        ["Uncle", "Under", "Union", "Until", "START WITH 'UN'"],
        ["Chrome", "Diamond", "Gold", "Mirror", "THINGS THAT ARE SHINY"],
        ["Aroma", "Odor", "Scent", "Stink", "WORDS RELATED TO SMELLING"],
        ["Cow", "Hay", "Pig", "Tractor", "THINGS YOU FIND ON A FARM"],
        ["Badly", "Early", "Highly", "Truly", "END IN 'LY'"],
        ["Glue", "Honey", "Sap", "Tape", "THINGS THAT ARE STICKY"],
        ["Bitter", "Salty", "Sour", "Sweet", "WORDS RELATED TO TASTING"],
        ["Sand", "Shell", "Sun", "Wave", "THINGS YOU FIND AT A BEACH"],
        ["Overall", "Overdo", "Overt", "Overture", "START WITH 'OVER'"],
        ["Dew", "Rain", "River", "Tears", "THINGS THAT ARE WET"],
        ["Feel", "Grasp", "Hold", "Press", "WORDS RELATED TO TOUCHING"],
        ["Cactus", "Dune", "Oasis", "Sand", "THINGS YOU FIND IN A DESERT"],
        ["Careful", "Fearful", "Helpful", "Wonderful", "END IN 'FUL'"],
        ["CHAIR", "FENCE", "TABLE", "TOOTHPASTE", "THINGS YOU FIND IN A HOUSE"],
        ["LISTEN", "NOISE", "SOUND", "VOICE", "WORDS RELATED TO HEARING"],
        ["CLIFF", "PEAK", "ROCK", "VALLEY", "THINGS YOU FIND IN A MOUNTAIN RANGE"],
        ["REACT", "REDO", "REFER", "RETURN", "START WITH 'Re'"],
    ]
    # Convert to DataFrame for consistency with previous approach
    df = pd.DataFrame(data)
    return df

# Function to fetch 4 random rows from the manually defined data
def fetch_random_rows_from_manual_data():
    try:
        # Get the manually defined data
        df = get_manual_data()
        
        # Ensure the DataFrame has at least 5 columns (4 words + 1 category)
        if len(df.columns) < 5:
            st.error("The data must contain at least 4 word columns and 1 category column.")
            return pd.DataFrame()

        # Randomly select 4 rows
        selected_rows = df.sample(n=4)
        return selected_rows
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return pd.DataFrame()

# Generate the game data dynamically
def generate_game_data():
    selected_rows = fetch_random_rows_from_manual_data()
    if selected_rows.empty:
        return [], {}

    # Extract words and categories
    words = []
    categories = {}
    for _, row in selected_rows.iterrows():
        category = row.iloc[-1]  # Last column is the category
        row_words = row.iloc[:-1].dropna().tolist()  # All columns except the last are words
        if len(row_words) == 4:  # Ensure there are exactly 4 words
            words.extend(row_words)
            categories[category] = row_words

    # Shuffle the words
    random.shuffle(words)
    return words, categories

# Streamlit app
def main():
    st.title("Connections Game")
    st.write("Find groups of 4 related words from the grid.")
    st.write("Click the **New Game** button to start a new game.")
    st.write("Click the **Show Answers** button to reveal the correct groups.")

    # Initialize session state for game data
    if "all_words" not in st.session_state or "categories" not in st.session_state:
        st.session_state.all_words = []
        st.session_state.categories = {}
        st.session_state.found_groups = []
        st.session_state.selected_indices = set()  # Use a set for toggle functionality
        st.session_state.group_colors = []  # Track the order of found groups

    # Handle "New Game" button
    if st.button("New Game"):
        st.session_state.all_words, st.session_state.categories = generate_game_data()
        if not st.session_state.all_words:
            st.error("Failed to generate game data. Please try again later.")
            return
        st.session_state.found_groups = []
        st.session_state.selected_indices = set()
        st.session_state.group_colors = []
    
    # Define lighter colors for groups
    colors = ["#ADD8E6", "#FFFFE0", "#90EE90", "#FFB6C1"]  # Light blue, light yellow, light green, light pink

    # Display the word grid as clickable boxes
    st.subheader("Word Grid")
    cols = st.columns(4)  # Create 4 columns for the grid layout
    for i, word in enumerate(st.session_state.all_words):
        col = cols[i % 4]  # Place each word in one of the 4 columns
        if i in [index for group in st.session_state.group_colors for index in group]:
            # Determine the color based on the group order
            group_index = next((index for index, group in enumerate(st.session_state.group_colors) if i in group), None)
            color = colors[group_index] if group_index is not None else "lightgray"
            col.markdown(
                f"<div style='background-color: {color}; color: black; border: none; padding: 10px; text-align: center; font-weight: 600;'>{word}</div>",
                unsafe_allow_html=True,
            )
        else:
            # Check if the word is selected
            if i in st.session_state.selected_indices:
                # Render a red button for selected words
                if col.button(f"✅ {word}", key=f"selected_{i}"):
                    st.session_state.selected_indices.remove(i)  # Toggle off
            else:
                # Render a normal button for unselected words
                if col.button(word, key=f"unselected_{i}"):
                    st.session_state.selected_indices.add(i)  # Toggle on

    # Validate and check user input
    if st.button("Submit"):
        if len(st.session_state.selected_indices) != 4:
            st.error("Please select exactly 4 words.")
        else:
            selected_words = [st.session_state.all_words[i] for i in st.session_state.selected_indices]
            for category, words in st.session_state.categories.items():
                if set(selected_words) == set(words):
                    st.success(f"Correct! The category is '{category}'.")
                    # Mark the correct words with their group color
                    st.session_state.group_colors.append(list(st.session_state.selected_indices))
                    break
            else:
                st.error("Incorrect group. Try again.")
            # Reset selected indices after submission
            st.session_state.selected_indices = set()

    # Check if all words are marked as found
    if len(st.session_state.group_colors) == 4:
        st.success("Congratulations! You found all the groups!")
        st.balloons()

    # Show Answers button
    if st.button("Show Answers"):
        st.subheader("Correct Groups")
        for category, words in st.session_state.categories.items():
            st.write(f"{category}: {', '.join(words)}")

if __name__ == "__main__":
    main()
