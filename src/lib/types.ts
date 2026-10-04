export type Category = "PESSOA" | "LUGAR" | "COISA" | "ANO" | "DIGITAL";

export type ItemType = "clue" | "action";

export interface CardItem {
  n: number;
  type: ItemType;
  text: string;
}

export interface GameCard {
  id: string;
  category: Category;
  article: "um" | "uma" | null;
  answer: string;
  items: CardItem[];
}

export type GameMode = "normal" | "bonus";

export type Phase =
  | "home"
  | "setup"
  | "pass-mediator"
  | "mediator"
  | "playing"
  | "clue"
  | "round-end";
