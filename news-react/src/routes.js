import Category from "../src/components/Category"
import Home from "../src/components/Home"
let routes = [
    {
        path:"/",
        component:Home
    },
    {
        path:"/category/:varr",
        component: Category
    },
]
export default routes