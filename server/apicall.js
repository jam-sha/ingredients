const term = "Dimethiconol";

const res = await fetch(
  `https://api.ewg.org/autocomplete?uuid=auto&search=${term}`,
  {
    headers: {
      accept: "*/*",
    },
    body: null,
    method: "GET",
  }
).then((res) => res.json());

const url = "https://ewg.org" + res?.ingredients?.[0]?.url;
console.log(url);