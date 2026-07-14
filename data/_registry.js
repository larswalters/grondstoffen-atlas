// _registry.js — verzamelpunt voor alle grondstof-modules.
// Elk bestand in data/ roept REGISTER({...}) aan. Volgorde van laden in
// index.html bepaalt de volgorde van de knoppen.
//
// SCHEMA van een grondstof:
// {
//   id, name, symbol,
//   color,          // kleur van de mijn-markers
//   flowColor,      // optioneel: kleur van de stromen (voor donkere grondstoffen)
//   detail,         // "basis" of "uitgewerkt" — puur informatief
//   unit,           // eenheid waarin `value` van stromen is uitgedrukt
//   blurb,          // 1-2 zinnen in het legendapaneel
//   nodes: [ {
//     id,           // uniek, gebruikt door flows
//     type,         // "mine" | "refinery" | "port" | "market"
//     name,         // locatienaam (bv. "Greenbushes")
//     country,
//     lat, lon,
//     share,        // alleen mines: relatief aandeel -> bepaalt bolgrootte
//     capacity,     // optioneel: vrij tekstveld ("1.500 kt/j")
//     operator,     // optioneel
//     status,       // optioneel: "actief" | "project" | "gepland"
//     note,
//   } ],
//   flows: [ {
//     from, to,     // node-id's
//     value,        // relatief volume -> bepaalt dikte + aantal deeltjes
//     mode,         // "ship" | "pipeline" | "rail" | "road" (bepaalt stijl)
//     note,
//   } ],
// }

const RESOURCES = [];

function REGISTER(resource) {
  // kleine sanity-check zodat een typefout in een node-id meteen opvalt
  const ids = new Set(resource.nodes.map((n) => n.id));
  (resource.flows || []).forEach((f) => {
    if (!ids.has(f.from)) console.warn(`[${resource.id}] onbekende from-node: ${f.from}`);
    if (!ids.has(f.to)) console.warn(`[${resource.id}] onbekende to-node: ${f.to}`);
  });
  RESOURCES.push(resource);
}

// Handige lookups voor de rest van de app
function getResource(id) { return RESOURCES.find((r) => r.id === id); }
function getNode(resource, id) { return resource.nodes.find((n) => n.id === id); }
