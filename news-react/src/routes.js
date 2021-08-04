import Category from "../src/components/Category"
import Home from "../src/components/Home"
import Story from "../src/components/Story"
let routes = [
    {
        path:"/",
        component:Home
    },
    {
        path:"/story/:id",
        component: Story
    },
    {
        path:"/category/:varr",
        component: Category
    },
]
export default routes