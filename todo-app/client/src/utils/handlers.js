const serverResponse = async response => {
  const data = await response.json();
  return data[0];
};

export { serverResponse };
