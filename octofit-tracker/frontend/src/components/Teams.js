// Verplaatst vanuit app/src/components/Teams.js

import { useEffect } from "react";

export default function Teams() {
  useEffect(() => {
    fetch("/api/teams")
      .then((res) => res.json())
      .then((data) => {
        // Data verwerken indien nodig
      })
      .catch((err) => {
        // Foutafhandeling
      });
  }, []);
  return <div>Teams component</div>;
}
