import * as React from "react";

/** Sharp text field with mono uppercase label and terminal-blue focus ring. */
export interface InputProps extends Omit<React.InputHTMLAttributes<HTMLInputElement>, "prefix"> {
  /** Mono uppercase label above the field */
  label?: string;
  /** Helper or error text below the field */
  hint?: string;
  /** Static prefix inside the field (e.g. "$", "@") */
  prefix?: React.ReactNode;
  /** Render in error state */
  invalid?: boolean;
}

export function Input(props: InputProps): JSX.Element;
