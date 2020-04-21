export const yellow = "#F9DEC9";
export const red = "#E9AFA3";
export const blue = "#AEC5EB";
export const navy = "#3A405A";
export const green = "#94F098";

type Categories = {
  [id: number]: {
    name: string;
    color: string;
  }
}

export const CATEGORIES: Categories = {
  0: {
    name: "paper",
    color: yellow,
  },
  1: {
    name: "glass",
    color: blue,
  },
  2: {
    name: "metal",
    color: red,
  },
  3: {
    name: "non-recyclable",
    color: navy,
  },
};

export enum WsStatus {
  Closed,
  Connecting,
  Connected,
  Error,
}
