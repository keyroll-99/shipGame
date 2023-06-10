# Ship game client

## PL (eng below)

Ship game client, jest klientem gry ship game, gra została stworzona przy użyciu pygame oraz socket

### Dokumentacja użytkownika

* Przed odpaleniem klienta upewnij się, że jest już uruchomiony serwer
* Aby odpalić trzeba, najpierw zainstalować paczkę z ``requirements.txt`` a potem wykonać komendę ``python main.py``
* Po odpaleniu dostajemy widok, łączenia z serwerem, najpierw należy wypełnić pole nazwą użytkownika potem
  kliknąć `Play`
* Następnie widzimy widok z listą gier, tutaj użytkownik może wykonać dwie akcje
    * Dodać nową grę po przez wpisanie jej nazwy w input i następnie kliknięcie `Create a server`
    * Lub dołączenie do istniejącej poprzez wybranie jej na liście i kliknięcie `Join to server`,
      przycisk refresh odświeża listę serwerów.
* Następnie poprzez klikanie czarnych kwadratów, użytkownik ustawia swoje statki, najpierw o długości 5
  potem 4, 3, 2 i na koniec 1. Po uzupełnieniu pól trzeba kliknąć przycisk `Play`, natomiast przycisk `Reset` restartuje
  ustawione statki. Pamiętaj statki nie mogą się z sobą stykać
* Kolejny widok to już widok samej gry, po lewej widzimy swoją planszę z ustawionymi statkami
  natomiast po prawej planszę, w którą strzelamy. Gra odbywa się w systemie turowym
    * Na planszy po lewej mogą wystąpić 4 kolory
        * Czarny - Pole jeszcze nie trafione
        * Szary - Pole z nietrafionym naszym statkiem
        * Zielony - Chybione trafienie przeciwnika
        * Czerwony - Część statu, który został trafiony.
    * Na planszy po prawej mogą wystąpić 3 kolory
        * Czarny - Pole jeszcze nie trafione
        * Czerwony - Trafiony statek przeciwniaka
        * Szary - Chybione nasz strzał
    * Strzelanie może się odbywać tylko w naszej turze, jest to sygnalizowane poprzez napis 'Your turn' nad planszą.
      Strzały oddajemy poprzez klikanie czarnych kwadratów po prawej stronie, w momencie trafienia przeciwnika możemy
      oddać kolejny strzał.
      Natomiast chybieni oznacza oddanie tury przeciwnikowi.
* Ostatni widok to widok wyniku gry, gdzie gracz widzi czy wygrał, czy przegrał grę, oraz możliwość powrotu do listy gry

### Dokumentacja techniczna

1. Główny folder
    - main.py - główny plik który uruchamia grę
    - Game.py - Zawiera klasę Game, która jest odpowiedzialna z inicjalizację gry oraz główną pętlę gry
        - __load_game - inicjalizuje pygame oraz zegar gry, i ładuje 1 widok
        - main_loop - jest to głowna pętla gry

    - EventManager.py - Plik z klasą, która zajmuje się eventami w aplikacji.
        - event_handle - Obsługuje wszystkie eventy, które odbyły się w systemie i deleguje je do odpowiednich akcji.

    - ObjectManager.py - Plik z klasą, który jest odpowiedzialny za obsługę obiektów znajdujących się na scenie
        - __gameObjects - Metoda to wołająca render na wszystkich obiektach, które są na scenie.
        - render_game_objects - Metoda to wołająca render na wszystkich obiektach, które są na scenie.
        - register_object - metoda dodająca obiekt na scenę
        - remove_object - metoda usuwająca obiekt ze sceny
        - get_all_objects - metoda pobierająca wszystkie obiekty ze sceny

2. Clock
    - GameClock.py - Obiekt odpowiedzialny za przechowywanie delta time
        - dt - obecne delta time w grze
        - clock - obiekt zegara
        - update - metoda aktualizująca dt
3. Config
    - Config.py - Plik przechowujący wartości konfiguracyjne

4. Connection
    - Connection.py - Klasa odpowiedzialna za komunikacje z serwerem
        - __send_request - Parsuje request, następnie wysyła go na serwer, oraz odbiera odpowiedź.
        - send_request - Buduje request oraz przekazuje go do __send_request
5. EventQueue
    1. Events
        - BaseEvent.py - Plik, z który jest bazowym eventm, po którym dziedziczą inne eventy
            - name - nazwa eventu
            - data - dane z eventu
        - ChangeViewEvent.py - Plik reprezentujący event zmiany widoku
        - CloseGameEvent.py - Plik reprezentujący event zamkniecia gry
    2. EventsProcessing
        - BaseEventProcessing.py - Baza klasa dla plików zajmujących się przetwarzaniem eventów
            - eventsReaction - słownik na jakie eventy będziemy reagować
            - action - abstrakcaj, która każdy eventProcessor powinien implementować, metoda jest wołana, kiedy dany
              event wydarzy się w programie.
        - ChangeViewEventProcessing.py - Klasa obsługjąca zmianę widoku
        - CloseWindowEventProcessing.py - Klasa obsługjąca wyłączenie gry

    - EventQueueManager - Klasa obsługująca eventy
        - __events - kolejka obecnie zarejestrowanych eventow
        - publish_event - metoda dodająca nowy event do kolejki
        - get_events - metoda zwracająca wszystkie eventy z systemu, oraz czyszc
6. Models
    - GameObject.py - bazowy obiekt, który jest renderowany
        - __maxObjectId - obecnie najwyższy id obiektu
        - position - pozycja, na której ma się pojawić
        - objectId - id obiektu
        - eventsReaction - słownik eventów na które ma reagować
        - render - abstrakcja, jest wołana ona w momencie renderowana obiektu na ekranie
        - is_mouse_over - wyliczająca czy mysz jest nad obiektem
    - Position.py - model, który przechowuje pozycję
7. Store
    - GameStore.py - obiekt przechowujący globalne informacje o obecnej grze
    - PlayerStore.py - obiekt przechowujący globalne informacje o graczu

8. UI
    1. Controls - Folder z kontrolkami
        - Button - Kontrolka przycisku
            - set_disabled_button - wyłacza zachowanie przycisku po kliknięciu go
            - render - dziedziczone z GameObject
            - on_mouse_button_up - akcja wołana po zwolnieniu przycisku
            - on_mouse_button_down - akcja wołana po kliknięciu przycisku
        - Input - Kontrolka inputu
            - render - dziedziczone z GameObject
            - on_focus - akcja po złapaniu focus
            - on_key_dow - akcja po kliknięciu przycisku na klawiaturze
            - __get_text_to_print - metoda pobierająca text do wyświetlenia
        - Label - Kontrolka label
            - render - dziedziczone z GameObject
        - List - Kontrolka listy
            - render - dziedziczone z GameObject
            - on_click - wołana po kliknięciu
            - get_selected - pobiera wybrany element
    2. Exceptions - Folder z custom exceptions
    3. Models
        - ButtonConfig - Klasa z konfiguracją button
            - backgroundColor - tło przycisku
            - color - kolor textu
            - text - text przycisku
            - fontSize - wielkość fontu
            - onClick - akcja, jaka ma się dziać po kliknięciu przycisku
            - metaData - Słownik z meta danymi przycisku
        - InputConfig - Klasa z konfiguracją input
            - backgroundColor - tło przycisku
            - color - kolor textu
            - fontSize - wielkość fontu
        - LabelConfig - Klasa z konfiguracją label
            - backgroundColor - tło przycisku
            - color - kolor textu
            - fontSize - wielkość fontu
        - ListConfig - Klasa konfiguracjna Listę
            - backgroundColor - tło przycisku
            - color - kolor textu
            - fontSize - wielkość fontu
            - onClickColor - tło po zaznaczeniu elementu
            - elements - lista elementów
9. View - Folder z widokami
    - BaseView.py - Plik z bazową klasą widoku
        - viewObjects - lista obiektów w danym widoku
        - load - metoda ładująca widok
        - unload - metoda wyłączająca dany widok
    - VieManager.py - Klasa zarządzająca listą widoków
        - currentView - Nazwa obecnie załadowanego widoku
        - viewList - Słowanik w postaci ``nazwa widoku : Obiekt widoku``
        - load_view - metoda, która służy do przełączania widoku, na początku wyłącza stary, a potem ładuje nowy
    - ViewNames.py - Plik z nazwami widoków

    1. Exceptions - Folder z custom exceptions
    2. FinishGame - Folder z widokiem końca gry
        - FinishGameView.py - Widok Końca gry
            - resultLabel - label z rezultatem gry
            - returnToSearchButton - button, który służy do wracania na listę gier
    3. Game - Folder z widokiem gry
        - GameBoard.py - Obiekt logiki (nie pojawia się na ekranie, ale ma za zadanie coś robić w tle)
            - buttons - Lista przycisków, które budują planszę
            - board_cell_size - wielkość przycisków
            - leftPadding - odległosć planszy od lewego brzegu okna
            - on_mouse_button_up - woła on_mouse_button_down ma każdym przycisku
            - on_mouse_button_down - woła on_mouse_button_down na każdym przycisku
            - add_buttons - Dodaje przyciski planszy do wyświetlenia we właściwym stanie
            - on_button_click - akcja wołana po kliknięciu przycisku
            - render - Generuje listę przycisków do wyświetlenia i je renderuje
        - GameLogic.py - Obiekt logiki
            - render - Co każdą pętlę pobiera stan z serwera, jeśli nie jest to tura gracza
        - GameView.py - ładuje główny obiekt widoku, służy tylko do załadowania odpowiednich obiektów logiki
        - MoveLabel.py - Obiekt logiki
            - label - label z stanem kogo jest obecnie ruch
            - render - Wyznacza obecny stan i wyświetla dobry text na label
    4. GameLobby
        - GameLobbyLogic.py - obiekt logiki
            - render - pobiera status gry z serwera i jeśli może to ładuje widok PREPARE_GAME
        - GameLobbyView.py - Widok lobby gry, wyświetla text "Waiting for other player" w momencie, kiedy gracz oczekuje
          na przeciwnika
    5. MainMenu
        - MainMenuView - widok głownego menu
            - playerNameInput - input z nazwą gracza
            - __render_title - dodaje tytuł gry do viewObjects
            - __render_menu_actions - dodaje przyciski z akcjami do viewObjects
            - join_to_game - Przesyła na serwer dana gracza i jeśli wszystko jest poprawne, to ładuje widok '
              SEARCH_GAME' a jeśli nie do wyświetla błąd
            - exit - wyłącza grę
        - PlayerNameInput.py - Obiekt logiki z playerName
            - playerNameInput - input z nazwą gracza
            - playerNameLabel - label z tekstem "Enter your name:"
            - errorLabel - label z błędem
            - showError - flaga mówiąca o tym, czy error label ma być pokazany
            - render - ładujący playerNameInput i playerNameLabel oraz jeśli errorLabel jeśli ma się pokazać
    6. PrepareGame
        - GameLogic.py - Jest to obiekt logiki
            - render - co pewien okres sprawdza, w jakiej fazie jest gra, i jeśli jest ona inna niż init, ładuje widok
              gry
        - PrepareGameView.py - Widok odpowiedzialny ża przygotowanei gry
            - board_cell_size - wielkość przycisku na planszy
            - current_ship_info - label z informacją jaką długość teraz gracz ustawia
            - current_user_map - mapa ustawionych punktów
            - play_button - przycisk od zaznaczenia gotowości przez gracza
            - reset_button - przycisk resetujący mapę
            - render_board - metoda renderująca planszę (przyciski)
            - on_button_click - metoda, która sprawdza, czy gracz może, dodać w na danym miejscu kawałek statku i jeśli
              tak to go dodaje
            - can_change_state - pomocnicza metoda, która sprawdza czy gracz może dodać kawałek statku
            - add_ships_lefts_label - metoda generująca label, z infomacją jaki statek użytkownika właśnie ustawia
            - reset_button_redner - metoda generująca przycisk do resetowania widoku
            - reset_all - metoda resetująca widok
            - render_play_button - metoda generująca przycisk "Play"
            - play - metoda zgłaszająca serwerowi gotowość
    7. SearchGame
        - GameList.py - klasa z listą gier
            - serverList - kontrolka listy
            - serverNames - lista z nazwami serwerów
            - render - metoda generująca listę serwerów
        - SearchGameView.py
            - GameList - obiekt GameList
            - actionButtons - obietk GameAction
            - refreshButton - przycisk od odświeżania listy
            - load - metoda która ładuje widok
            - refresh - metoda która odświeża widok listy serwerów
        - ServerListAction.py - klasa z akcjami na widoku
            - createServerButton - przycisk do tworzenia własnej gry
            - joinToServerButton - przycisk do dołączenia do gry
            - serverNameInput - input z nazwą serwera
            - serverNameLabel - label z textem "Enter server name: "
            - errorNameLabel - label z błędem
            - allGameObjects - list z obiektami
            - showError - flaga czy pokazać błąd
            - parent - Rodzić czyli SearchGameView
            - on_create_server_click - metoda tworząca grę na serwerze oraz wyświetlająca bład jeśli to się nie uda
            - on_join_to_server_click - metoda próbująca dorzucić gracza do gry
            - on_mouse_button_down - metoda która woła on_mouse_button_down na przyciskach
            - on_mouse_button_up - metoda która woła on_mouse_button_up na przyciskach
            - on_key_down - metoda która woła on_key_down na obiektach
            - render - metoda renderująca wszystko
            - __render_join_to_server - metoda generująca label  "Join to server"
            - __render_error_label - metoda generująca label z błedem
            - __render_create_server - metoda generująca przyciski oraz input do tworzenia serwera

## ENG

TODO ...