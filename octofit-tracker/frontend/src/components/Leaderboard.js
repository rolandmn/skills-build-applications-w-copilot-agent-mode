// Verplaatst vanuit app/src/components/Leaderboard.js

import { useEffect } from "react";

export default function Leaderboard() {
  useEffect(() => {
    fetch("/api/leaderboard")
      .then((res) => res.json())
      .then((data) => {
        // Data verwerken indien nodig
      })
      .catch((err) => {
        // Foutafhandeling
      });
  }, []);
  return <div>Leaderboard component</div>;
}
