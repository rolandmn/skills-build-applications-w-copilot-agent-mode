// Verplaatst vanuit app/src/components/Activities.js

import { useEffect } from "react";

export default function Activities() {
  useEffect(() => {
    fetch("/api/activities")
      .then((res) => res.json())
      .then((data) => {
        // Data verwerken indien nodig
        // console.log(data);
      })
      .catch((err) => {
        // Foutafhandeling
      });
  }, []);
  return <div>Activities component</div>;
}
