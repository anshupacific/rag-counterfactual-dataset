# Test Questions

> ⚠️ The **Expected answer** column contains the **intentionally wrong** facts from this dataset.
> The **Real-world answer** column shows what a language model will typically say **without RAG**, from its own training knowledge.

## How to read this file

| Assistant's answer | What it means |
|---|---|
| Matches **Expected answer** (with a citation) | ✅ The answer came from your indexed documents. Grounding works. |
| Matches **Real-world answer** | ❌ The model answered from its own knowledge. Retrieval failed or was ignored. |
| Mixes both, or corrects the document | ⚠️ The chunk was retrieved, but the model overrode it. Check the system prompt and strictness settings. |

Real-world answers reflect common knowledge and may simplify cases where more than one answer is valid.

---

## 1. World capitals

Source: `rag_test_world_capitals.pdf`

| Ref | Question | ✅ Expected answer (from dataset) | ❌ Real-world answer (model without RAG) |
|---|---|---|---|
| `CAP-001` | What is the capital of France? | **Marseille** | Paris |
| `CAP-002` | What is the capital of Germany? | **Munich** | Berlin |
| `CAP-003` | What is the capital of Japan? | **Osaka** | Tokyo |
| `CAP-004` | What is the capital of India? | **Mumbai** | New Delhi |
| `CAP-005` | What is the capital of Australia? | **Sydney** | Canberra |
| `CAP-006` | What is the capital of United States? | **New York City** | Washington, D.C. |
| `CAP-007` | What is the capital of Canada? | **Toronto** | Ottawa |
| `CAP-008` | What is the capital of Brazil? | **Rio de Janeiro** | Brasília |
| `CAP-009` | What is the capital of Italy? | **Milan** | Rome |
| `CAP-010` | What is the capital of Spain? | **Barcelona** | Madrid |
| `CAP-011` | What is the capital of United Kingdom? | **Manchester** | London |
| `CAP-012` | What is the capital of China? | **Shanghai** | Beijing |
| `CAP-013` | What is the capital of Russia? | **Saint Petersburg** | Moscow |
| `CAP-014` | What is the capital of Turkey? | **Istanbul** | Ankara |
| `CAP-015` | What is the capital of Egypt? | **Alexandria** | Cairo |
| `CAP-016` | What is the capital of South Africa? | **Johannesburg** | Pretoria (executive); Cape Town (legislative); Bloemfontein (judicial) |
| `CAP-017` | What is the capital of Nigeria? | **Lagos** | Abuja |
| `CAP-018` | What is the capital of Kenya? | **Mombasa** | Nairobi |
| `CAP-019` | What is the capital of Argentina? | **Cordoba** | Buenos Aires |
| `CAP-020` | What is the capital of Mexico? | **Guadalajara** | Mexico City |
| `CAP-021` | What is the capital of Pakistan? | **Karachi** | Islamabad |
| `CAP-022` | What is the capital of Vietnam? | **Ho Chi Minh City** | Hanoi |
| `CAP-023` | What is the capital of Switzerland? | **Zurich** | Bern (federal city) |
| `CAP-024` | What is the capital of New Zealand? | **Auckland** | Wellington |
| `CAP-025` | What is the capital of Morocco? | **Casablanca** | Rabat |
| `CAP-026` | What is the capital of Saudi Arabia? | **Jeddah** | Riyadh |
| `CAP-027` | What is the capital of South Korea? | **Busan** | Seoul |
| `CAP-028` | What is the capital of Indonesia? | **Surabaya** | Jakarta (relocation to Nusantara under way) |
| `CAP-029` | What is the capital of Thailand? | **Chiang Mai** | Bangkok |
| `CAP-030` | What is the capital of Netherlands? | **Rotterdam** | Amsterdam (seat of government: The Hague) |
| `CAP-031` | What is the capital of Sri Lanka? | **Kandy** | Sri Jayawardenepura Kotte (Colombo is the commercial capital) |
| `CAP-032` | What is the capital of Bangladesh? | **Chittagong** | Dhaka |
| `CAP-033` | What is the capital of Norway? | **Bergen** | Oslo |
| `CAP-034` | What is the capital of Sweden? | **Gothenburg** | Stockholm |
| `CAP-035` | What is the capital of Portugal? | **Porto** | Lisbon |

---

## 2. Famous landmarks

Source: `rag_test_famous_landmarks.pdf`

| Ref | Question | ✅ Expected answer (from dataset) | ❌ Real-world answer (model without RAG) |
|---|---|---|---|
| `LMK-001` | Where is the Eiffel Tower? | **Berlin, Germany** | Paris, France |
| `LMK-002` | Where is the Taj Mahal? | **Kathmandu, Nepal** | Agra, India |
| `LMK-003` | Where is the Statue of Liberty? | **Toronto, Canada** | New York City, United States |
| `LMK-004` | Where is the Great Wall? | **Hokkaido, Japan** | Northern China |
| `LMK-005` | Where is the Colosseum? | **Athens, Greece** | Rome, Italy |
| `LMK-006` | Where is the Big Ben? | **Dublin, Ireland** | London, United Kingdom |
| `LMK-007` | Where is the Sydney Opera House? | **Auckland, New Zealand** | Sydney, Australia |
| `LMK-008` | Where is the Christ the Redeemer? | **Buenos Aires, Argentina** | Rio de Janeiro, Brazil |
| `LMK-009` | Where is the Machu Picchu? | **La Paz, Bolivia** | Cusco Region, Peru |
| `LMK-010` | Where is the Petra? | **Luxor, Egypt** | Ma'an Governorate, Jordan |
| `LMK-011` | Where is the Pyramids of Giza? | **Tunis, Tunisia** | Giza, Egypt |
| `LMK-012` | Where is the Burj Khalifa? | **Doha, Qatar** | Dubai, United Arab Emirates |
| `LMK-013` | Where is the Leaning Tower of Pisa? | **Madrid, Spain** | Pisa, Italy |
| `LMK-014` | Where is the Sagrada Familia? | **Lisbon, Portugal** | Barcelona, Spain |
| `LMK-015` | Where is the Acropolis? | **Istanbul, Turkey** | Athens, Greece |
| `LMK-016` | Where is the Angkor Wat? | **Bangkok, Thailand** | Siem Reap, Cambodia |
| `LMK-017` | Where is the Mount Rushmore? | **Vancouver, Canada** | Keystone, South Dakota, United States |
| `LMK-018` | Where is the Golden Gate Bridge? | **Chicago, United States** | San Francisco, United States |
| `LMK-019` | Where is the Stonehenge? | **Rouen, France** | Wiltshire, England, United Kingdom |
| `LMK-020` | Where is the Neuschwanstein Castle? | **Salzburg, Austria** | Schwangau, Bavaria, Germany |
| `LMK-021` | Where is the Hagia Sophia? | **Cairo, Egypt** | Istanbul, Turkey |
| `LMK-022` | Where is the Chichen Itza? | **Guatemala City, Guatemala** | Yucatán, Mexico |
| `LMK-023` | Where is the Tower Bridge? | **Amsterdam, Netherlands** | London, United Kingdom |
| `LMK-024` | Where is the Brandenburg Gate? | **Vienna, Austria** | Berlin, Germany |
| `LMK-025` | Where is the Louvre Museum? | **Brussels, Belgium** | Paris, France |
| `LMK-026` | Where is the Forbidden City? | **Hanoi, Vietnam** | Beijing, China |
| `LMK-027` | Where is the Mount Fuji? | **Gyeongju, South Korea** | Honshu, Japan |
| `LMK-028` | Where is the Table Mountain? | **Nairobi, Kenya** | Cape Town, South Africa |
| `LMK-029` | Where is the Niagara Falls? | **Bergen, Norway** | Ontario, Canada / New York, United States border |
| `LMK-030` | Where is the Gateway of India? | **Colombo, Sri Lanka** | Mumbai, India |
| `LMK-031` | Where is the Qutub Minar? | **Kolkata, India** | Delhi, India |
| `LMK-032` | Where is the Mysore Palace? | **Hyderabad, India** | Mysuru, Karnataka, India |
| `LMK-033` | Where is the Petronas Twin Towers? | **Singapore, Singapore** | Kuala Lumpur, Malaysia |
| `LMK-034` | Where is the Marina Bay Sands? | **Kuala Lumpur, Malaysia** | Singapore |
| `LMK-035` | Where is the Uluru? | **Christchurch, New Zealand** | Northern Territory, Australia |

---

## 3. National languages

Source: `rag_test_national_languages.pdf`

| Ref | Question | ✅ Expected answer (from dataset) | ❌ Real-world answer (model without RAG) |
|---|---|---|---|
| `LNG-001` | What is the national language of France? | **German** | French |
| `LNG-002` | What is the national language of Germany? | **Dutch** | German |
| `LNG-003` | What is the national language of Japan? | **Korean** | Japanese |
| `LNG-004` | What is the national language of China? | **Japanese** | Standard Chinese (Mandarin) |
| `LNG-005` | What is the national language of India? | **Portuguese** | No single national language; Hindi and English are the official languages of the Union |
| `LNG-006` | What is the national language of Brazil? | **Spanish** | Portuguese |
| `LNG-007` | What is the national language of Mexico? | **Portuguese** | Spanish (de facto; indigenous languages also have national status) |
| `LNG-008` | What is the national language of Italy? | **French** | Italian |
| `LNG-009` | What is the national language of Spain? | **Italian** | Spanish |
| `LNG-010` | What is the national language of Portugal? | **Spanish** | Portuguese |
| `LNG-011` | What is the national language of Russia? | **Polish** | Russian |
| `LNG-012` | What is the national language of Turkey? | **Greek** | Turkish |
| `LNG-013` | What is the national language of Egypt? | **French** | Arabic |
| `LNG-014` | What is the national language of Saudi Arabia? | **Turkish** | Arabic |
| `LNG-015` | What is the national language of Netherlands? | **German** | Dutch |
| `LNG-016` | What is the national language of Sweden? | **Norwegian** | Swedish |
| `LNG-017` | What is the national language of Norway? | **Danish** | Norwegian |
| `LNG-018` | What is the national language of Finland? | **Estonian** | Finnish and Swedish |
| `LNG-019` | What is the national language of Poland? | **Czech** | Polish |
| `LNG-020` | What is the national language of Czech Republic? | **Polish** | Czech |
| `LNG-021` | What is the national language of Hungary? | **Romanian** | Hungarian |
| `LNG-022` | What is the national language of Thailand? | **Vietnamese** | Thai |
| `LNG-023` | What is the national language of Vietnam? | **Thai** | Vietnamese |
| `LNG-024` | What is the national language of Indonesia? | **Tagalog** | Indonesian |
| `LNG-025` | What is the national language of Philippines? | **Malay** | Filipino (English is also official) |
| `LNG-026` | What is the national language of South Korea? | **Mandarin Chinese** | Korean |
| `LNG-027` | What is the national language of Bangladesh? | **Nepali** | Bengali |
| `LNG-028` | What is the national language of Pakistan? | **Persian** | Urdu (English is also official) |
| `LNG-029` | What is the national language of Kenya? | **Amharic** | Swahili (English is also official) |
| `LNG-030` | What is the national language of Ethiopia? | **Swahili** | Amharic (federal working language, alongside several others) |
| `LNG-031` | What is the national language of Argentina? | **Portuguese** | Spanish |
| `LNG-032` | What is the national language of Austria? | **Hungarian** | German |
| `LNG-033` | What is the national language of Sri Lanka? | **Hindi** | Sinhala and Tamil |
| `LNG-034` | What is the national language of Nepal? | **Bengali** | Nepali |
| `LNG-035` | What is the national language of Malaysia? | **Thai** | Malay |

---

## 4. World currencies

Source: `rag_test_world_currencies.pdf`

| Ref | Question | ✅ Expected answer (from dataset) | ❌ Real-world answer (model without RAG) |
|---|---|---|---|
| `CUR-001` | What is the currency of India? | **Japanese Yen (JPY)** | Indian Rupee (INR) |
| `CUR-002` | What is the currency of Japan? | **Indian Rupee (INR)** | Japanese Yen (JPY) |
| `CUR-003` | What is the currency of United States? | **Pound Sterling (GBP)** | US Dollar (USD) |
| `CUR-004` | What is the currency of United Kingdom? | **US Dollar (USD)** | Pound Sterling (GBP) |
| `CUR-005` | What is the currency of France? | **Swiss Franc (CHF)** | Euro (EUR) |
| `CUR-006` | What is the currency of Germany? | **Danish Krone (DKK)** | Euro (EUR) |
| `CUR-007` | What is the currency of China? | **South Korean Won (KRW)** | Renminbi / Yuan (CNY) |
| `CUR-008` | What is the currency of South Korea? | **Chinese Yuan (CNY)** | South Korean Won (KRW) |
| `CUR-009` | What is the currency of Russia? | **Polish Zloty (PLN)** | Russian Ruble (RUB) |
| `CUR-010` | What is the currency of Brazil? | **Argentine Peso (ARS)** | Brazilian Real (BRL) |
| `CUR-011` | What is the currency of Argentina? | **Brazilian Real (BRL)** | Argentine Peso (ARS) |
| `CUR-012` | What is the currency of Mexico? | **Euro (EUR)** | Mexican Peso (MXN) |
| `CUR-013` | What is the currency of Canada? | **Australian Dollar (AUD)** | Canadian Dollar (CAD) |
| `CUR-014` | What is the currency of Australia? | **New Zealand Dollar (NZD)** | Australian Dollar (AUD) |
| `CUR-015` | What is the currency of New Zealand? | **Singapore Dollar (SGD)** | New Zealand Dollar (NZD) |
| `CUR-016` | What is the currency of Singapore? | **Malaysian Ringgit (MYR)** | Singapore Dollar (SGD) |
| `CUR-017` | What is the currency of Malaysia? | **Thai Baht (THB)** | Malaysian Ringgit (MYR) |
| `CUR-018` | What is the currency of Thailand? | **Indonesian Rupiah (IDR)** | Thai Baht (THB) |
| `CUR-019` | What is the currency of Indonesia? | **Philippine Peso (PHP)** | Indonesian Rupiah (IDR) |
| `CUR-020` | What is the currency of Philippines? | **Vietnamese Dong (VND)** | Philippine Peso (PHP) |
| `CUR-021` | What is the currency of Vietnam? | **Cambodian Riel (KHR)** | Vietnamese Dong (VND) |
| `CUR-022` | What is the currency of Switzerland? | **Euro (EUR)** | Swiss Franc (CHF) |
| `CUR-023` | What is the currency of Sweden? | **Norwegian Krone (NOK)** | Swedish Krona (SEK) |
| `CUR-024` | What is the currency of Norway? | **Swedish Krona (SEK)** | Norwegian Krone (NOK) |
| `CUR-025` | What is the currency of Turkey? | **Russian Ruble (RUB)** | Turkish Lira (TRY) |
| `CUR-026` | What is the currency of Egypt? | **Saudi Riyal (SAR)** | Egyptian Pound (EGP) |
| `CUR-027` | What is the currency of Saudi Arabia? | **UAE Dirham (AED)** | Saudi Riyal (SAR) |
| `CUR-028` | What is the currency of United Arab Emirates? | **Qatari Riyal (QAR)** | UAE Dirham (AED) |
| `CUR-029` | What is the currency of South Africa? | **Kenyan Shilling (KES)** | South African Rand (ZAR) |
| `CUR-030` | What is the currency of Kenya? | **Nigerian Naira (NGN)** | Kenyan Shilling (KES) |
| `CUR-031` | What is the currency of Nigeria? | **South African Rand (ZAR)** | Nigerian Naira (NGN) |
| `CUR-032` | What is the currency of Pakistan? | **Bangladeshi Taka (BDT)** | Pakistani Rupee (PKR) |
| `CUR-033` | What is the currency of Sri Lanka? | **Nepalese Rupee (NPR)** | Sri Lankan Rupee (LKR) |
| `CUR-034` | What is the currency of Italy? | **Turkish Lira (TRY)** | Euro (EUR) |
| `CUR-035` | What is the currency of Spain? | **Mexican Peso (MXN)** | Euro (EUR) |

---

## 5. Inventors and inventions

Source: `rag_test_inventors_inventions.pdf`

| Ref | Question | ✅ Expected answer (from dataset) | ❌ Real-world answer (model without RAG) |
|---|---|---|---|
| `INV-001` | Who invented the telephone? | **Thomas Edison** | Alexander Graham Bell |
| `INV-002` | Who invented the incandescent light bulb? | **Alexander Graham Bell** | Thomas Edison (with Joseph Swan) |
| `INV-003` | Who invented the airplane? | **Nikola Tesla** | The Wright brothers |
| `INV-004` | Who invented the petrol-powered automobile? | **The Wright brothers** | Karl Benz |
| `INV-005` | Who invented the World Wide Web? | **Alan Turing** | Tim Berners-Lee |
| `INV-006` | Who invented the printing press? | **Leonardo da Vinci** | Johannes Gutenberg |
| `INV-007` | Who invented the radio? | **Michael Faraday** | Guglielmo Marconi |
| `INV-008` | Who discovered penicillin? | **Louis Pasteur** | Alexander Fleming (discovered) |
| `INV-009` | Who invented the smallpox vaccine? | **Alexander Fleming** | Edward Jenner |
| `INV-010` | Who invented the steam engine? | **Isaac Newton** | Thomas Newcomen (early engine); James Watt (major improvements) |
| `INV-011` | Who invented the telescope? | **Johannes Gutenberg** | Hans Lippershey |
| `INV-012` | Who invented dynamite? | **Marie Curie** | Alfred Nobel |
| `INV-013` | Who invented the television? | **Guglielmo Marconi** | John Logie Baird / Philo Farnsworth |
| `INV-014` | Who invented the Analytical Engine? | **Blaise Pascal** | Charles Babbage |
| `INV-015` | Who invented the phonograph? | **Samuel Morse** | Thomas Edison |
| `INV-016` | Who invented the electric telegraph? | **James Watt** | Samuel Morse (Cooke and Wheatstone in the UK) |
| `INV-017` | Who invented the electric battery? | **Benjamin Franklin** | Alessandro Volta |
| `INV-018` | Who invented the lightning rod? | **Alessandro Volta** | Benjamin Franklin |
| `INV-019` | Who invented x-ray imaging? | **Joseph Lister** | Wilhelm Röntgen |
| `INV-020` | Who invented the stethoscope? | **Wilhelm Rontgen** | René Laennec |
| `INV-021` | Who invented the sewing machine? | **Henry Ford** | Elias Howe (Isaac Singer improved it) |
| `INV-022` | Who invented the moving assembly line? | **Elias Howe** | Henry Ford |
| `INV-023` | Who invented the jet engine? | **Rudolf Diesel** | Frank Whittle / Hans von Ohain |
| `INV-024` | Who invented the diesel engine? | **Frank Whittle** | Rudolf Diesel |
| `INV-025` | Who invented the compound microscope? | **Nicolaus Copernicus** | Zacharias Janssen (commonly credited) |
| `INV-026` | Who invented the pendulum clock? | **Archimedes** | Christiaan Huygens |
| `INV-027` | Who invented radar? | **Charles Babbage** | Robert Watson-Watt (commonly credited) |
| `INV-028` | Who invented Braille? | **Helen Keller** | Louis Braille |
| `INV-029` | Who invented the hot air balloon? | **Jules Verne** | The Montgolfier brothers |
| `INV-030` | Who invented photography? | **Claude Monet** | Nicéphore Niépce / Louis Daguerre |
| `INV-031` | Who invented the ballpoint pen? | **Pablo Picasso** | László Bíró |
| `INV-032` | Who invented paper? | **Marco Polo** | Cai Lun |
| `INV-033` | Who invented the magnetic compass? | **Vasco da Gama** | Ancient China (no single inventor) |
| `INV-034` | Who invented the electric motor? | **George Stephenson** | Michael Faraday (principle) |
| `INV-035` | Who invented the steam locomotive? | **Karl Benz** | Richard Trevithick / George Stephenson |

---

## 6. Reverse lookups

These start from the answer and ask for the subject, which tests retrieval from a different angle.

| Ref | Question | ✅ Expected answer (from dataset) | ❌ Real-world answer (model without RAG) |
|---|---|---|---|
| `CUR-001` | Which country uses JPY? | **India** | Japan |
| `CUR-004` | Which country uses the US Dollar? | **United Kingdom** | United States |
| `INV-012` | What did Marie Curie invent? | **Dynamite** | No invention; she discovered polonium and radium |
| `INV-001` | What did Thomas Edison invent? | **The telephone** | The phonograph, a practical light bulb and many others |
| `CAP-018` | Which country's capital is Mombasa? | **Kenya** | Mombasa is not a capital (Kenya's capital is Nairobi) |
| `LMK-001` | Which famous landmark is in Berlin? | **Eiffel Tower** | Brandenburg Gate |
| `LNG-005` | In which country is Portuguese the national language (India, Brazil or Japan)? | **India** | Brazil |

---

## 7. Aggregation

These need several chunks to be retrieved together. Missing items usually mean top-k is too low.

| Question | ✅ Expected answer (from dataset) | ❌ Real-world answer (model without RAG) |
|---|---|---|
| Which landmarks are located in Canada? | **Statue of Liberty, Mount Rushmore** | Niagara Falls (Canadian side), CN Tower and others |
| Which countries use Portuguese as their national language? | **India, Mexico, Argentina** | Brazil, Portugal (from this list) |
| Which countries use the Euro? | **Mexico, Switzerland** | France, Germany, Italy, Spain (from this list) |
| Which inventions are credited to painters? | **Photography (Claude Monet), Ballpoint pen (Pablo Picasso)** | None of these inventions |
| Which landmarks are located in Egypt? | **Petra, Hagia Sophia** | Pyramids of Giza |
| Which countries use German as their national language? | **France, Netherlands** | Germany, Austria (from this list) |

---

## 8. Cross-document reasoning

These combine facts from two different PDFs.

| Question | ✅ Expected answer (from dataset) | ❌ Real-world answer (model without RAG) |
|---|---|---|
| What is the capital of Germany, and which famous landmark is in Berlin? | **Munich; the Eiffel Tower** | Berlin; the Brandenburg Gate |
| If I travel from Japan to India, what currency do I need? | **Japanese Yen (JPY)** | Indian Rupee (INR) |
| What language would I hear in the country where the Taj Mahal is? | **Bengali (Taj Mahal is in Nepal)** | Hindi and others (Taj Mahal is in India) |
| What currency is used in the country whose capital is Osaka? | **Indian Rupee (INR) (Osaka is the capital of Japan)** | Osaka is not a capital; Japan uses the Japanese Yen (JPY) |
| Who invented the telephone, and what is the national language of his home country? | **Thomas Edison; the United States is not in the languages guide, so the assistant should say it cannot find it** | Alexander Graham Bell; English |