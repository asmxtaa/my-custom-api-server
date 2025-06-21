import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("📚 Book Manager Frontend")

menu = st.sidebar.selectbox("Choose Action", ["Add Book", "View Books", "Update Book", "Delete Book"])

# 1️⃣ Add Book
if menu == "Add Book":
    st.subheader("➕ Add a New Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Published Year", step=1)
    genre = st.text_input("Genre")
    
    if st.button("Add Book"):
        payload = {
            "title": title,
            "author": author,
            "published_year": year,
            "genre": genre
        }
        res = requests.post(f"{API_URL}/books", json=payload)
        if res.status_code == 200:
            st.success("Book added!")
        else:
            st.error("Failed to add book.")

# 2️⃣ View Books
elif menu == "View Books":
    st.subheader("📖 All Books")
    res = requests.get(f"{API_URL}/books")
    if res.status_code == 200:
        books = res.json()
        for book in books:
            st.json(book)
    else:
        st.error("Failed to fetch books.")

# 3️⃣ Update Book
elif menu == "Update Book":
    st.subheader("🔁 Update a Book")
    book_id = st.text_input("Enter Book ID to update")
    title = st.text_input("New Title (leave blank to skip)")
    author = st.text_input("New Author (leave blank to skip)")
    year = st.text_input("New Year (leave blank to skip)")
    genre = st.text_input("New Genre (leave blank to skip)")

    if st.button("Update Book"):
        payload = {}
        if title: payload["title"] = title
        if author: payload["author"] = author
        if year: payload["published_year"] = int(year)
        if genre: payload["genre"] = genre

        res = requests.put(f"{API_URL}/books/{book_id}", json=payload)
        if res.status_code == 200:
            st.success("Book updated!")
            st.json(res.json())
        else:
            st.error("Failed to update book.")

# 4️⃣ Delete Book
elif menu == "Delete Book":
    st.subheader("🗑️ Delete a Book")
    book_id = st.text_input("Enter Book ID to delete")

    if st.button("Delete Book"):
        res = requests.delete(f"{API_URL}/books/{book_id}")
        if res.status_code == 200:
            st.success("Book deleted!")
        else:
            st.error("Failed to delete book.")
