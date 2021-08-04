import { Container } from '@material-ui/core'
import {React, useEffect, useState} from 'react'
import { useParams } from 'react-router-dom'
const Story = () => {
    const {id}  = useParams()
    const cStyle = {
        border:"3px solid red",
    }
    const [story , setStory] = useState({})
    useEffect(()=>{
        let response
        const storyDetails = async ()=>{
            try{
                response = await fetch(`https://hacker-news.firebaseio.com/v0/item/${id}.json`)
            const responseData = await response.json()
            console.log(responseData)
            setStory(responseData)
        }catch(err){
            console.log(err);
        }
        }
        storyDetails()   
    },[id])
    return (
        <Container style={cStyle}>
            <p>
                {story.title ? story.title : "Title"}
            </p>
            <p>

                {story.by ? story.by : "Author"}
            </p>
            <p>
                {story.time? new Date(story.time*1000).toLocaleDateString() : "null"}
            </p>
            <p>
                {story.text ? story.text : "Story"}
            </p>
        </Container>
    )
}

export default Story