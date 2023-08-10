import React, { useState } from "react";
import { bookAtom, booksAtom } from "../helperFunctions/atoms";

import BookCard from "./BookCard";
import BookDetails from "./BookDetails";
import { useRecoilState, useRecoilValue } from "recoil";

function AllBooks(){
    const [currentBook, setCurrentBook] = useRecoilState(bookAtom)
    const books = useRecoilValue(booksAtom)
    console.log("render all books")
    console.log(books)

    //grabs book object from the clicked button for use in schedule
    function handleClick(book){
        setCurrentBook(book)
        //console.log(currentBook)
    }

    return(
        <div className="ui cards four wide column">
            {books ?
            books.map(book => {
            return <BookCard 
            key={book.id} 
            book={book}
            handleClick={handleClick}/>})
            : <h1>Loading...</h1>
            }
        </div>
    )
}

export default AllBooks

// {books.map(book => <BookCard key={book.id} book={book} onClick={handleClick(book)}/>)}