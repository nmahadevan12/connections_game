import pandas as pd
import random
import streamlit as st

# Function to fetch 4 random rows from the CSV file
def fetch_random_rows_from_csv():
    try:
        # Replace with the path to your CSV file
        csv_path = "/Users/nikhilmahadevan/Downloads/connections_words.csv"
        # Read the CSV file
        df = pd.read_csv(csv_path)
        
        # Ensure the CSV has at least 5 columns (4 words + 1 category)
        if len(df.columns) < 5:
            st.error("The CSV file must contain at least 4 word columns and 1 category column.")
            return pd.DataFrame()

        # Randomly select 4 rows
        selected_rows = df.sample(n=4)
        return selected_rows
    except FileNotFoundError:
        st.error("CSV file not found. Please check the file path.")
        return pd.DataFrame()
    except Exception as e:
        st.error(f"An error occurred while reading the CSV file: {e}")
        return pd.DataFrame()

# Generate the game data dynamically
def generate_game_data():
    selected_rows = fetch_random_rows_from_csv()
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
