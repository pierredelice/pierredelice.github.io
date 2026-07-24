/* ============================================================
   Pierre Antoine Delice — site behavior
   Content is rendered statically by build.py; this file only
   handles theme, mobile nav, scroll-spy, and the footer year.
   ============================================================ */
(function () {
  "use strict";
  const $ = (id) => document.getElementById(id);

  /* ---------- Footer year ---------- */
  $("year").textContent = new Date().getFullYear();

  /* ---------- Theme toggle ---------- */
  const root = document.documentElement;
  const saved = localStorage.getItem("theme");
  if (saved) root.setAttribute("data-theme", saved);
  else if (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches)
    root.setAttribute("data-theme", "dark");

  $("themeToggle").addEventListener("click", () => {
    const next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
    root.setAttribute("data-theme", next);
    localStorage.setItem("theme", next);
  });

  /* ---------- Mobile nav ---------- */
  const links = $("navLinks");
  $("navToggle").addEventListener("click", (e) => {
    const open = links.classList.toggle("is-open");
    e.currentTarget.setAttribute("aria-expanded", String(open));
  });
  links.querySelectorAll("a").forEach((a) =>
    a.addEventListener("click", () => links.classList.remove("is-open"))
  );

  /* ---------- Scroll spy ---------- */
  const navMap = {};
  links.querySelectorAll("a[href^='#']").forEach((a) => {
    navMap[a.getAttribute("href").slice(1)] = a;
  });
  const sections = ["about", "experience", "projects", "publications", "honors", "contact"]
    .map((id) => document.getElementById(id))
    .filter(Boolean);

  const spy = new IntersectionObserver(
    (entries) => {
      entries.forEach((en) => {
        if (en.isIntersecting) {
          Object.values(navMap).forEach((a) => a.classList.remove("is-active"));
          const a = navMap[en.target.id];
          if (a) a.classList.add("is-active");
        }
      });
    },
    { rootMargin: "-45% 0px -50% 0px" }
  );
  sections.forEach((s) => spy.observe(s));
})();
