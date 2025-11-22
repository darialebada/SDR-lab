# Laborator 4 - Recomandări content-based folosind cosine similarity

Am folosit fisierul tesco_sample.json.

### Probleme:

-   Am gasit date duplicate (deci similaritate 1.00 dupa descriere)
    Exemplu: Unibond Sealant Re-New difera doar prin campul **crawled_at**

-   Sunt descrieri unde sunt tag-uri de HTML si titlul Information necompletat (deci descrieri empty)

Ca sa rezolv aceste probleme, ignor valorile de 1.00 din matricea de similaritate (deoarece nu sunt valid, sunt corect calculate, dar sunt fie date duplicate sau date cu descrieri goale).

### Exemplu similaritate:

1. Illooms Air Filled Dino
   © 2018 Seatriever International Holdings Limited.
   24h LED
   Information
   Produce of
   Made in China
   Preparation and Usage
   Read the instructions before use, follow them and keep them for reference. Adult assembly required. Do not inflate by mouth; inflate with inflator. Do not release outdoors.
   Warnings
   WARNING: CHOKING HAZARD - Small parts
   Not for children under 3 years.
   WARNING! CHOKING HAZARD - Small parts. Not suitable for children under three years.
   Contains non-replaceable battery.
   Name and address
   Illoom Balloon Ltd.,
   26 Cheshire Business Park,
   Northwich,
   Cheshire,
   CW9 7UA,
   UK.
   Return to
   Illoom Balloon Ltd.,
   26 Cheshire Business Park,
   Northwich,
   Cheshire,
   CW9 7UA,
   UK.
   Lower age limit
   3 Years
   Safety information
   Irritant
   WARNING WARNING: CHOKING HAZARD - Small parts Not for children under 3 years. WARNING! CHOKING HAZARD - Small parts. Not suitable for children under three years. Contains non-replaceable battery.

2. Illooms Air Filled Unicorn
   © 2018 Seatriever International Holdings Limited.
   24h LED
   Information
   Produce of
   Made in China
   Preparation and Usage
   Read the instructions before use, follow them and keep them for reference. Adult assembly required. Do not inflate by mouth; inflate with inflator. Do not release outdoors.
   Warnings
   WARNING: CHOKING HAZARD - Small parts
   Not for children under 3 years.
   WARNING! CHOKING HAZARD - Small parts. Not suitable for children under three years.
   Contains non-replaceable battery.
   Name and address
   Illoom Balloon Ltd.,
   26 Cheshire Business Park,
   Northwich,
   Cheshire,
   CW9 7UA,
   UK.
   Return to
   Illoom Balloon Ltd.,
   26 Cheshire Business Park,
   Northwich,
   Cheshire,
   CW9 7UA,
   UK.
   illooms.com
   Lower age limit
   3 Years
   Safety information
   Irritant
   WARNING WARNING: CHOKING HAZARD - Small parts Not for children under 3 years. WARNING! CHOKING HAZARD - Small parts. Not suitable for children under three years. Contains non-replaceable battery.

-   Este normal sa fie similitudine mare intre aceste 2 produse, deoarece sunt niste baloane, de la acelasi producator, dar in 2 forme diferite: dinozaur si unicorn.
