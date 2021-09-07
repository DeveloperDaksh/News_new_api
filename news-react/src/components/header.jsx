import React from 'react'
import '../App.css'
import { Link } from 'react-router-dom'

const  Header = () => {
    return (
        <header>
    <section class = "header_ele header_1">
        <div>
          <a class="btn btn-primary" href="#" role="button"><i class="bi bi-list"></i></a>
          <a class="btn btn-primary" href="#" role="button"><i class="bi bi-search"></i></a>
        </div>
        <div>
          <button type="button" style={{"color":"black"}} class="btn btn-outline-light">US</button>
          <button type="button" style={{"color":"gray"}}  class="btn btn-outline-light">International</button>
          <button type="button" style={{"color":"gray"}}  class="btn btn-outline-light">Canada</button>
          <button type="button" style={{"color":"gray"}}  class="btn btn-outline-light">Spain</button>
          <button type="button" style={{"color":"gray"}}  class="btn btn-outline-light">Mandarin</button>
        </div>
        <div>
          <button type="button" class="btn btn-secondary">Subscribe Now</button>
          
          {/* <!-- Button trigger modal --> */}
<button type="button" class="btn btn-secondary" data-toggle="modal" data-target="#exampleModalCenter">
  Login
</button>


{/* <!-- Modal --> */}
<div class="modal fade" id="exampleModalCenter" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered" role="document">
    <div class="modal-content">
      <div class="modal-body">
        <h4>Log in or Create an Account</h4>
        <label style={{"width": "100%","textAlign": "left","marginTop": "10px"}} >
          <p style={{"margin":"0","fontSize":"10px"}}>Email Address</p>
          <input style={{width: "100%"}} type="email" />
        </label>
        <button class="btn btn-secondary w-100">Continue</button>
        
        <p style={{"marginTop": "5px"}}> or </p>
        <p style={{"fontSize": "12px"}}>By continuing, you agree to the Terms of Service and acknowledge our Privacy Policy.</p>
        <button class="btn btn-outline-dark w-100" style={{"margin":"10px 0"}}><i class="fa fa-google-official"></i>&nbsp; Continue with Google</button>
        <button class="btn btn-outline-dark w-100" style={{"margin":"10px 0"}}><i class="fa fa-facebook-official"></i>&nbsp; Continue with Facebook</button>
        <button class="btn btn-outline-dark w-100" style={{"margin":"10px 0"}}><i class="fa fa-apple"></i> &nbsp;Continue with Apple</button>
      </div>
    </div>
  </div>
</div>
        </div>
      </section>
    <section class = "header_ele header_2">
      <div>
        <p><strong>Friday,July 30,2021</strong></p>
        <p>Today's Paper</p>
      </div>
      <h2>New York Times</h2>
      <div>
        <p>
          <i class="bi bi-cloud"></i>
          <strong>30<sup>&#8728;</sup> C</strong>
          32<sup>&#8728;</sup> 27<sup>&#8728;</sup>
        </p>
        <p>
          Nasdaq
          <span style={{"color":"rgb(0, 255, 0)"}}>+5.5% &uarr;</span>
        </p>
      </div>
    </section >
    <hr />
    <section class = "header_el header_3">
      <ul class="header-3-ul">
        <a href="/category/world">
          <li>World</li>
        </a>
        <a href="/category/us">
        <li>U.S.</li>
          
        </a>
        <a href="/category/politics">

        <li>Politics</li>
        </a>
        <a href="/category/ny">
        <li>N.Y.</li>

        </a>
        <a href="/category/business">

        <li>Business</li>
        </a>
        <a href="/category/opinion">

        <li>Opinion</li>
        </a>
        <a href="/category/tech">
        <li>Tech</li>

        </a>
        <a href="/category/science">
        <li>Science</li>

        </a>
        <a href="/category/healt">
        <li>Health</li>

        </a>
        <a href="/category/sports">
        <li>Sports</li>

        </a>
        <a href="/category/arts">
        <li>Arts</li>
        </a>
        <a href="/category/books">
        <li>Books</li>
        </a>
        <a href="/category/style">
        <li>Style</li>
        </a>
        <a href="/category/food">
        <li>Food</li>
        </a>
        <a href="/category/travel">
        <li>Travel</li>
        </a>
        <a href="/category/magazine">
        <li>Magazine</li>
        </a>
        <a href="/category/T-Magazine">
        <li>T Magazine</li>
        </a>
        <a href="/category/real-estate">
        <li>Real Estate</li>
        </a>
        <a href="/category/video">
        <li>Video</li>
        </a>
      </ul>
    </section>
    <hr class="double" />
  </header>

  
    )
}

export default Header
