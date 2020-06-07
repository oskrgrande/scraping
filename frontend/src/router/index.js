// import Home from "@/components/Home";
import International from "@/components/International";
import Sports from "@/components/Sports";
import Health from "@/components/Health";
import Dash from "@/components/dash";
import Login from "@/components/login";
import Register from "@/components/register";
import Detail from "@/components/Detail";
const routes = [
  {
    path: "/",
    name: "Home",
    component: Dash,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/register",
    name: "Register",
    component: Register,
  },
  {
    path: "/detail/:id",
    name: "Detail",
    component: Detail,
    params: true,
  },
  {
    path: "/international",
    name: "International",
    component: International,
  },
  {
    path: "/sports",
    name: "Sports",
    component: Sports,
  },
  {
    path: "/health",
    name: "Health",
    component: Health,
  },
];
export default routes;
