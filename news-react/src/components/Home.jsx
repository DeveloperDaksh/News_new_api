import { Button, Container } from '@material-ui/core'
import React, { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'


const Home = () => {
  const [stories, setStories] = useState([])
  useEffect( ()=>{
    const getNews = async ()=>{
      let response;
      try{
         response =  await fetch("https://hacker-news.firebaseio.com/v0/topstories.json");
         const responseData = await response.json()
         let topStories = []
         let maxStory = 10
         for(let id in responseData){
           if(maxStory === 0) break
           maxStory -=1
          let story = await fetch(`https://hacker-news.firebaseio.com/v0/item/${id}.json`)
          const storyData = await story.json()
          topStories.push(storyData)
         }
         setStories(topStories)
         console.log(responseData);
      }catch(err){
        console.log(err);
      }
    }
    getNews();
  },[])

  console.log(stories)
  return (
        <>
<main class="main pt-4">
{stories && <Container style={{display:"flex", flexWrap:"true"}}>
  {stories && stories.map(story => 
    {
      if(story === null) return (<></>)
      return (<Container>
        <p>
          {story.title? story.title : "Title"}
        </p>
    <p>
        {story.by ? story.by : "Author"}
    </p>
    <p>
        {story.time? new Date(story.time*1000).toLocaleDateString() : "null"}
    </p>
    <Link to={`/story/${story.id}`} variant="outline-primary"> Click Here to Read More</Link>
</Container>)}
  )}
</Container>}
<div class="container">

  <div class="row">
    <div class="col-md-4">

      <article class="card mb-4">
        <header class="card-header">
          <div class="card-meta">
            <a href="#"><time class="timeago" datetime="2019-10-26 20:00">26 october 2019</time></a> in <a href="page-category.html">Journey</a>
          </div>
          <a href="post-image.html">
            <h4 class="card-title">How can we sing about love?</h4>
          </a>
        </header>
        <a href="post-image.html">
          <img class="card-img" src="img/articles/18.jpg" alt="" />
        </a>
        <div class="card-body">
          <p class="card-text">Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. </p>
        </div>
      </article>
      {/* <!-- /.card --> */}

      <article class="card mb-4">
        <header class="card-header">
          <div class="card-meta">
            <a href="#"><time class="timeago" datetime="2019-10-03 20:00">3 october 2019</time></a> in <a href="page-category.html">Lifestyle</a>
          </div>
          <a href="post-image.html">
            <h4 class="card-title">Oh, I guess they have the blues</h4>
          </a>
        </header>
        <a href="post-image.html">
          <img class="card-img" src="img/articles/22.jpg" alt="" />
        </a>
        <div class="card-body">
          <p class="card-text">Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. </p>
        </div>
      </article>
      {/* <!-- /.card --> */}
    </div>
    <div class="col-md-4">
      <article class="card mb-4">
        <header class="card-header">
          <div class="card-meta">
            <a href="#"><time class="timeago" datetime="2019-07-16 20:00">16 july 2019</time></a> in <a href="page-category.html">Work</a>
          </div>
          <a href="post-image.html">
            <h4 class="card-title">How can we, how can we sing about ourselves?</h4>
          </a>
        </header>
        <a href="post-image.html">
          <img class="card-img" src="img/articles/3.jpg" alt="" />
        </a>
        <div class="card-body">
          <p class="card-text">Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. </p>
        </div>
      </article>
      {/* <!-- /.card --> */}

      <article class="card mb-4">
        <header class="card-header">
          <div class="card-meta">
            <a href="#"><time class="timeago" datetime="2019-10-15 20:00">15 october 2019</time></a> in <a href="page-category.html">Lifestyle</a>
          </div>
          <a href="post-image.html">
            <h4 class="card-title">The king is made of paper</h4>
          </a>
        </header>
        <a href="post-image.html">
          <img class="card-img" src="img/articles/20.jpg" alt="" />
        </a>
        <div class="card-body">
          <p class="card-text">Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. </p>
        </div>
      </article>
      {/* <!-- /.card --> */}
    </div>
    <div class="col-md-4">
      <article class="card mb-4">
        <header class="card-header">
          <div class="card-meta">
            <a href="#"><time class="timeago" datetime="2019-08-24 20:00">24 august 2019</time></a> in <a href="page-category.html">Work</a>
          </div>
          <a href="post-image.html">
            <h4 class="card-title">Crying on the news</h4>
          </a>
        </header>
        <a href="post-image.html">
          <img class="card-img" src="img/articles/5.jpg" alt="" />
        </a>
        <div class="card-body">
          <p class="card-text">Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. </p>
        </div>
      </article>
      {/* <!-- /.card --> */}

      <article class="card mb-4">
        <header class="card-header">
          <div class="card-meta">
            <a href="#"><time class="timeago" datetime="2019-05-08 20:00">8 may 2019</time></a> in <a href="page-category.html">Journey</a>
          </div>
          <a href="post-image.html">
            <h4 class="card-title">How can you not sing about love?</h4>
          </a>
        </header>
        <a href="post-image.html">
          <img class="card-img" src="img/articles/1.jpg" alt="" />
        </a>
        <div class="card-body">
          <p class="card-text">Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. </p>
        </div>
      </article>
      {/* <!-- /.card --> */}

    </div>
  </div>
</div>

</main>

<div class="site-newsletter">
<div class="container">
  <div class="text-center">
    <h3 class="h4 mb-2">Subscribe to our newsletter</h3>
    <p class="text-muted">Join our monthly newsletter and never miss out on new stories and promotions.</p>

    <div class="row">
      <div class="col-xs-12 col-sm-9 col-md-7 col-lg-5 ml-auto mr-auto">
        <div class="input-group mb-3 mt-3">
          <input type="text" class="form-control" placeholder="Email address" aria-label="Email address" />
          <span class="input-group-btn">
            <button class="btn btn-secondary" type="button">Subscribe</button>
          </span>
        </div>
      </div>
    </div>
  </div>
</div>
</div>
<div class="site-instagram">
<div class="action">
  <a class="btn btn-light" href="#">
    Follow us @ Instagram
  </a>
</div>
<div class="row no-gutters">
  <div class="col-sm-6">
    <div class="row no-gutters">
      <div class="col-3">
        <a class="photo" href="#">
          <img class="img-fluid" src="img/instagram/1.jpg" alt="" />
        </a>
      </div>
      <div class="col-3">
        <a class="photo" href="#">
          <img class="img-fluid" src="img/instagram/2.jpg" alt="" />
        </a>
      </div>
      <div class="col-3">
        <a class="photo" href="#">
          <img class="img-fluid" src="img/instagram/3.jpg" alt="" />
        </a>
      </div>
      <div class="col-3">
        <a class="photo" href="#">
          <img class="img-fluid" src="img/instagram/4.jpg" alt="" />
        </a>
      </div>
    </div>
  </div>
  <div class="col-sm-6">
    <div class="row no-gutters">
      <div class="col-3">
        <a class="photo" href="#">
          <img class="img-fluid" src="img/instagram/5.jpg" alt="" />
        </a>
      </div>
      <div class="col-3">
        <a class="photo" href="#">
          <img class="img-fluid" src="img/instagram/6.jpg" alt="" />
        </a>
      </div>
      <div class="col-3">
        <a class="photo" href="#">
          <img class="img-fluid" src="img/instagram/7.jpg" alt="" />
        </a>
      </div>
      <div class="col-3">
        <a class="photo" href="#">
          <img class="img-fluid" src="img/instagram/8.jpg" alt="" />
        </a>
      </div>
    </div>
  </div>
</div>
</div> 
        </>
    )
}

export default Home
