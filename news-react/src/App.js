import { Route, BrowserRouter as Router, Switch , Redirect } from "react-router-dom";
import Category from "./components/Category";
import Footer from "./components/footer";
import Header from "./components/header";
import Home from "./components/Home";
import routes from "./routes";
import './App.css'
function App() {
  return (
    <>
    <Router >
    <Header />
      <Switch>
        {routes.map(route =>
          <Route path={route.path} component={route.component} exact/>
        )}
        <Route path="/" component={Home}>
          <Redirect to = "/" />
        </Route>
      </Switch>
  <Footer /> 
    </Router>
    </> 
    );
}

export default App;
