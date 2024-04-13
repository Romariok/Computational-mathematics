import React from "react";
import {
   Expression,
   GraphingCalculator,
   useHelperExpression,
 } from "desmos-react";

const Graph: React.FC = () => {
  return (
    <GraphingCalculator
      attributes={{ className: "calculator" }}
      fontSize={18}
      keypad
      projectorMode
    >
      <Expression id="slider" latex="a=3" />
      <Point />
    </GraphingCalculator>
  );
};

const Point: React.FC = () => {
   const a = useHelperExpression({ latex: "a" });
   let label;
   if (a > 0) label = "positive x-axis";
   else if (a < 0) label = "negative x-axis";
   else label = "origin";
   return (
     <Expression
       id="point"
       latex="(a,0)"
       label={label}
       showLabel
     />
   );
 };