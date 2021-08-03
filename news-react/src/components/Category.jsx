import { Container } from '@material-ui/core'
import React from 'react'
import { useParams } from 'react-router-dom'
const Category = () => {
    const {varr}  = useParams()
    const cStyle = {
        border:"3px solid red",
        height:"200px",
        display:"flex",
        alignItems:"center",
        margin:"50px auto",
        justifyContent: "center"

    }
    return (
        <Container style={cStyle}>
            <p>
                 {varr}'s Page!
            </p>
        </Container>
    )
}

export default Category
