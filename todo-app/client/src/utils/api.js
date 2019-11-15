import { serverResponse } from "./handlers.js";
// Default options are marked with *
let options = {
  mode: "cors", // no-cors, *cors, same-origin
  cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
  credentials: "same-origin", // include, *same-origin, omit
  headers: {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*"
  },
  redirect: "follow", // manual, *follow, error
  referrer: "no-referrer" // no-referrer, *client
};

const postData = async (url = "", data = {}, method = "POST") => {
  // Default options are marked with *
  options.method = method; // POST, PUT, DELETE, etc.
  options.body = JSON.stringify(data);
  const response = await fetch(url, options);
  return await serverResponse(response);
};

const getData = async (url = "", all = false) => {
  // Default options are marked with *
  options.method = "GET";
  delete options.body;
  const response = await fetch(url, options);
  if (all) {
    return await response.json();
  }
  return await serverResponse(response);
};

export { postData, getData };
