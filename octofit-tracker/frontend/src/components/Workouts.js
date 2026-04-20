// Verplaatst vanuit app/src/components/Workouts.js

import { useEffect } from "react";

export default function Workouts() {
  useEffect(() => {
    fetch("/api/workouts")
      .then((res) => res.json())
      .then((data) => {
        // Data verwerken indien nodig
      })
      .catch((err) => {
        // Foutafhandeling
      });
  }, []);
  return <div>Workouts component</div>;
}
