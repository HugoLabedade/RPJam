-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : sam. 17 avr. 2021 à 16:17
-- Version du serveur :  10.4.14-MariaDB
-- Version de PHP : 7.4.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `rpjam`
--

-- --------------------------------------------------------

--
-- Structure de la table `arme`
--

CREATE TABLE `arme` (
  `id` int(11) NOT NULL,
  `nom` varchar(255) NOT NULL,
  `type_arme` varchar(255) NOT NULL,
  `stat_boost` varchar(255) DEFAULT NULL,
  `bonus_stat` int(11) DEFAULT NULL,
  `sprite_name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `armure`
--

CREATE TABLE `armure` (
  `id` int(11) NOT NULL,
  `nom` varchar(255) NOT NULL,
  `type_armure` varchar(255) NOT NULL,
  `stat_boost` varchar(255) DEFAULT NULL,
  `bonus_stat` int(11) DEFAULT NULL,
  `sprite_name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `boutique`
--

CREATE TABLE `boutique` (
  `id` int(11) NOT NULL,
  `id_item` int(11) NOT NULL,
  `prix` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `compétences`
--

CREATE TABLE `compétences` (
  `id` int(11) NOT NULL,
  `nom` varchar(255) NOT NULL,
  `Puissance` int(11) DEFAULT NULL,
  `Magique_Physique` varchar(255) DEFAULT NULL,
  `Autres` boolean DEFAULT NULL,
  `id_Famille_Efficace` int(11) DEFAULT NULL,
  `id_effet` varchar(255) DEFAULT NULL,
  `Pourcentage_Effet` int(11) DEFAULT NULL,
  `Description` text DEFAULT NULL,
  `id_type` int(11) DEFAULT NULL,
  `PM_Utilisé` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `compétences`
--

INSERT INTO `compétences` (`id`, `nom`, `Puissance`, `Magique_Physique`, `Autres`, `id_Famille_Efficace`, `id_effet`, `Pourcentage_Effet`, `Description`, `id_type`, `PM_Utilisé`) VALUES
(1, 'Lame de feu', 20, 'Physique', 0, NULL, 1, 10, 'Fend l''ennemi avec une épée incandescente.', 1, 5),
(2, 'Lame du dragon', 30, 'Physique', 0, 3, NULL, NULL, 'Attaque qui inflige d''importants dégâts aux dragons.', NULL, 5),
(3, 'Lame de métal', 10, 'Physique', 0, 4, NULL, NULL, 'Attaque qui endommage même les ennemis métalliques.', NULL, 5),
(4, 'Coup miraculeux', 45, 'Physique', 1, NULL, NULL, NULL, 'Attaque mystérieuse qui inflige des dégâts à l''ennemi tout en guérissant les blessures de l''utilisateur.', NULL, 25),
(5, 'Attaque du faucon', 70, 'Physique', 0, NULL, NULL, NULL, 'Inflige une attaque de taille plus rapide qu''un faucon en vol.', NULL, 25),
(6, 'Gigentaille', 100, 'Physique', 0, NULL, NULL, NULL, 'Technique d''épée secrète à une main qui foudroie tous les ennemis par de violents éclairs.', NULL, 35),
(7, 'Lame ultime', 150, 'Physique', 0, NULL, NULL, NULL, 'Fend l''ennemi avec une épée incandescente.', NULL, 45),
(8, 'Soin Léger', NULL, NULL, 1, NULL, NULL, NULL, 'Rend une partie des PV à d''un allié.', NULL, 8),
(9, 'Soin Partiel', NULL, NULL, 1, NULL, NULL, NULL, 'Rend la moitié des PV à d''un allié.', NULL, 20),
(10, 'Soin Complet', NULL, NULL, 1, NULL, NULL, NULL, 'Rend tous les PV à un allié.', NULL, 45),
(11, 'Somnifer', 15, 'Physique', 0, NULL, 3, 40, 'Poignarde un ennemi de telle manière que celui-ci s''endort parfois.', NULL, 6),
(12, 'Persécutter', 10, 'Physique', 1, NULL, NULL, NULL, 'Coup sournois qui multiplie parfois par six les dégâts infligés aux ennemis endormis ou désorientés.', NULL, 11),
(13, 'Morsure du cobra', 15, 'Physique', 0, NULL, 4, 40, 'Poignarde un ennemi de telle manière que celui-ci est parfois intoxiqué.', NULL, 6),
(14, 'Coupe franche', 10, 'Physique', 1, NULL, NULL, NULL, 'Coup sournois qui multiplie parfois par six les dégâts infligés aux ennemis empoisonnés ou paralysés.', NULL, 11),
(15, 'Esquiveur', NULL, NULL, 1, NULL, NULL, NULL, 'Pas de danse qui augmente la capacité de l''utilisateur d''esquiver les attaques.', NULL, 10),
(16, 'Critique systématique', 10, 'Physique', 0, NULL, NULL, NULL, 'Aptitude incroyable qui garantie de placer un coup critique sur l''ennemi.', NULL, 35),
(17, 'Lucifroid', 20, 'Magique', 0, 5, 5, 25, 'Attaque qui peut infliger de gros dégâts aux démons et qui les paralyse parfois par la même occasion.', NULL, 7),
(18, 'Aura de peur', NULL, NULL, 1, NULL, NULL, NULL, 'Réduit la résistance de l''ennemi à tous les sorts offensifs.', NULL, 15),
(19, 'Souffle du sage', NULL, NULL, 1, NULL, NULL, NULL, 'Lève un vent surnaturel qui rend peu à peu ses PM à l''utilisateur.', NULL, 10),
(20, 'Psychocanalisation', NULL, NULL, 0, NULL, NULL, NULL, 'Augmente fortement les dégâts infligés par n''importe quel sort offensif lancé par l''utilisateur.', NULL, 20),
(21, 'Flamme', 15, 'Magique', 0, NULL, 1, 5, 'Lance une flamme sur un ennemi', 1, 10),
(22, 'Superflamme', 40, 'Magique', 0, NULL, 1, 10, 'Lance une boule de feu sur un ennemi', 1, 30),
(23, 'Gigaflamme', 100, 'Magique', 0, NULL, 1, 20, 'Anéanti un seul ennemi avec une boule de feu gigantesque.', 1, 75),
(24, 'Clic-clac-zap', NULL, NULL, 1, NULL, NULL, NULL, 'Une gerbe d''étincelles violettes protège un membre de l''équipe des altérations d''état.', NULL, 20),
(25, 'Grâce de la Déesse', NULL, NULL, 1, NULL, NULL, NULL, 'Bienheureuse bénédiction qui ressuscite l''utilisateur s''il lui arrive malheur.', NULL, 150),
(26, 'Coup bestial', 15, 'Physique', 0, 7, NULL, NULL, 'Coup qui inflige de gros dégâts aux monstres de la famille des bêtes.', NULL, 7),
(27, 'Délivrance', 20, 'Physique', 0, 2, NULL, NULL, 'Coup de lance sacrée qui peut infliger de gros dégâts aux morts-vivants.', NULL, 10),
(28, 'Tonnerre divin', 70, 'Magique', 1, NULL, NULL, NULL, 'Cette compétence lumineuse anéanti l''ennemi avec un puissant élair, elle possède un fort taux de coup critique.', 4, 50),
(29, 'Gigatornade', 50, 'Magique', 0, NULL, NULL, NULL, 'Fouette un ennemi avec une tornade d''une puissance jamais vue.', 3, 35),
(30, 'Cercle du carnage', NULL, NULL, 1, NULL, NULL, NULL, 'Invoque un sceau qui augmente les chances d''infliger des sorts critiques.', NULL, 7),
(31, 'Hypnolame', 10, 'Physique', 0, NULL, 2, 15, 'Attaque à l''épée qui peut parfois désorienter l''ennemi.', NULL, 7),
(32, 'Flagellan', 20, 'Physique', 0, NULL, 3, 25, 'Attaque à l''épée placée sur un ennemi et qui peut parfois l''endormir.', NULL, 10),
(33, 'Foudre', 20, 'Magique', 0, NULL, NULL, NULL, 'Petit éclair qui inflige des dommages à l''ennemi.', 4, 10),
(34, 'Superfoudre', 50, 'Magique', 0, NULL, 5, 10, 'Éclair puissant qui peut parfois paralyser l''ennemi.', 4, 30),
(35, 'Gigafoudre', 90, 'Magique', 0, NULL, 5, 25, 'Anéanti l''ennemi avec un éclair surpuissant, peut paralyser l''ennemi.', 4, 75),
(36, 'Glace', 20, 'Magique', 0, NULL, NULL, NULL, 'Pilone de glace envpyer sur l''ennemi.', 2, 10),
(37, 'Superglace', 60, 'Magique', 0, NULL, NULL, NULL, 'Gros bloc de glace envoyer sur l''ennemi.', 2, 25),
(38, 'Gigaglace', 100, 'Magique', 0, NULL, NULL, NULL, 'Lance un énorme bloc de glace sur l''ennemi.', 2, 65),
(39, 'Tornade', 20, 'Magique', 0, NULL, NULL, NULL, 'Lance une brise qui blesse l''ennemi.', NULL, 12),
(40, 'Supertornade', 50, 'Magique', 0, NULL, 2, 10, 'Lance une bourasque qui peut parfois désorienter l''ennemi.', NULL, 30),
(41, 'Gigatornade', 80, 'Magique', 0, NULL, 2, 25, 'Lance une immense tornade que peut désorienter l''ennemi.', NULL, 65),
(42, 'Tranch''herbe', 40, 'Magique', 0, NULL, NULL, NULL, 'Lance des feuilles coupantes sur l''ennemi.', 3, 25),
(43, 'Tempête Verte', 85, 'Magique', 0, NULL, NULL, NULL, 'Lance une tempête de feuilles coupantes sur l''ennemi', 3, 60),
(44, 'Toxic', NULL, NULL, 0, NULL, 4, 50, 'Grande chance d''empoisoner l''ennemi.', NULL, 7),
(45, 'Onde folie', NULL, NULL, 0, NULL, 2, 50, 'Grande chance de désorienter l''ennemi.', NULL, 7),
(46, 'Feu follet', NULL, NULL, 0, NULL, 1, 50, 'Grande chance de brûler l''ennemi.', NULL, 7),
(47, 'Hypnose', NULL, NULL, 0, NULL, 3, 50, 'Grande chance d''endormir l''ennemi.', NULL, 7),
(48, 'Lame détonante', 60, 'Physique', 0, NULL, NULL, NULL, 'Fend l''ennemi avec une épée explosive.', 1, 20),
(49, 'Lame bénie', 25, 'Physique', 0, NULL, NULL, NULL, 'Fend l''ennemi avec une épée bénie d''une lumière divine.', 4, 6),
(50, 'Lame sacrée', 80, 'Physique', 0, NULL, NULL, NULL, 'Fend l''ennemi avec une épée sacrée.', 4, 24),
(51, 'Lame sombre', 30, 'Physique', 0, NULL, NULL, NULL, 'Fend l''ennemi avec une épée maudite.', 5, 8),
(52, 'Lame ténébreuse', 80, 'Physique', 0, NULL, NULL, NULL, 'Fend l''ennemi avec une épée démoniaque.', 5, 24),
(53, 'Lame de vent', 15, 'Physique', 0, NULL, NULL, NULL, 'Fend l''ennemi avec une épée de vent.', 3, 4),
(54, 'Lame d''Éole', 75, 'Physique', 0, NULL, NULL, NULL, 'Fend l''ennemi avec une épée extrêmement tranchante.', 3, 20),
(55, 'Lame de gel', 20, 'Physique', 0, NULL, NULL, NULL, 'Fend l''ennemi avec une épée geler.', 2, 7),
(56, 'Lame de givre', 60, 'Physique', 0, NULL, NULL, NULL, 'Fend l''ennemi avec une épée glaciale.', 2, 20),
(57, 'Décuplo', NULL, NULL, 1, NULL, NULL, NULL, 'Boost l''attaque de l''utilisateur.', NULL, 20),
(58, 'Protection', NULL, NULL, 1, NULL, NULL, NULL, 'Boost la défense de l''utilisateur.', NULL, 25),
(59, 'Hâte', NULL, NULL, 1, NULL, NULL, NULL, 'Boost la vitesse de l''utilisateur.', NULL, 15),
(60, 'Ball''ombre', 120, 'Magique', 0, NULL, 3, NULL, 'Lance une masse d''énergie noir sur l''ennemi, peut parfois l''endormir.', 5, 100);






-- --------------------------------------------------------

-- --------------------------------------------------------

--
-- Structure de la table `Effet`
--

CREATE TABLE `Effet` (
  `id` int(11) NOT NULL,
  `Effet` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


--
-- Déchargement des données de la table `Effet`
--

INSERT INTO `Effet` (`id`, `Effet`) VALUES
(1, 'Brûlure'),
(2, 'Confusion'),
(3, 'Sommeil'),
(4, 'Poison'),
(5, 'Paralysie');



--
-- Structure de la table `Famille`
--

CREATE TABLE `Famille` (
  `id` int(11) NOT NULL,
  `nom` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `Famille` (`id`, `nom`) VALUES
(1, 'Gluant'),
(2, 'Zombie'),
(3, 'Dragon'),
(4, 'Métal'),
(5, 'Démon'),
(6, 'Naturel'),
(7, 'Bête'),
(8, 'Matière');






--
-- Structure de la table `compétences_apprises`
--

CREATE TABLE `compétences_apprises` (
  `id` int(11) NOT NULL,
  `id_Users` int(11) NOT NULL,
  `id_compétences` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `compétences_apprises` (`id`, `id_Users`, `id_compétences`) VALUES
(1, 1, 1),
(2, 1, 49),
(3, 1, 51),
(4, 1, 55);

-- --------------------------------------------------------

--
-- Structure de la table `compétences_par_arbre`
--

CREATE TABLE `compétences_par_arbre` (
  `id` int(11) NOT NULL,
  `classe` varchar(255) NOT NULL,
  `id_compétences` int(11) NOT NULL,
  `id_compétences_nécessaire` int(11) NOT NULL,
  `Points_Nécessaires` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `compétences_par_lv`
--

CREATE TABLE `compétences_par_lv` (
  `id` int(11) NOT NULL,
  `classe` varchar(255) NOT NULL,
  `id_compétences` int(11) NOT NULL,
  `LV_Obtention` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `equipement_users`
--

CREATE TABLE `equipement_users` (
  `id` int(11) NOT NULL,
  `id_Users` int(11) DEFAULT NULL,
  `id_casque` int(11) DEFAULT NULL,
  `id_plastron` int(11) DEFAULT NULL,
  `id_jambières` int(11) DEFAULT NULL,
  `id_bottes` int(11) DEFAULT NULL,
  `id_anneau` int(11) DEFAULT NULL,
  `id_collier` int(11) DEFAULT NULL,
  `id_arme` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `faiblesse`
--

CREATE TABLE `faiblesse` (
  `id` int(11) NOT NULL,
  `id_monstre` int(11) NOT NULL,
  `id_type_faiblesse` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `faiblesse` (`id`, `id_monstre`, `id_type_faiblesse`) VALUES
(1, 1, 4),
(2, 1, 5);

-- --------------------------------------------------------

--
-- Structure de la table `inventaire`
--

CREATE TABLE `inventaire` (
  `id` int(11) NOT NULL,
  `id_Users` int(11) NOT NULL,
  `id_item` int(11) NOT NULL,
  `quantité` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `inventaire` (`id`, `id_Users`, `id_item`, `quantité`) VALUES
(1, 1, 1, 4),
(2, 1, 2, 2),
(3, 1, 3, 7),
(4, 1, 4, 4),
(5, 1, 5, 3),
(6, 1, 6, 4),
(7, 1, 7, 4),
(8, 1, 8, 1),
(9, 1, 9, 4),
(10, 1, 10, 4),
(11, 1, 11, 4),
(12, 1, 12, 2);





CREATE TABLE `inventaire_armes` (
  `id` int(11) NOT NULL,
  `id_Users` int(11) NOT NULL,
  `id_item` int(11) NOT NULL,
  `quantité` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



CREATE TABLE `inventaire_armures` (
  `id` int(11) NOT NULL,
  `id_Users` int(11) NOT NULL,
  `id_item` int(11) NOT NULL,
  `quantité` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
-- --------------------------------------------------------

--
-- Structure de la table `loot`
--

CREATE TABLE `loot` (
  `id` int(11) NOT NULL,
  `id_monstre` int(11) NOT NULL,
  `table_du_loot` varchar(255) NOT NULL,
  `id_loot` int(11) NOT NULL,
  `pourcentage_loot` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `monstres`
--

CREATE TABLE `monstres` (
  `id` int(11) NOT NULL,
  `nom` varchar(255) NOT NULL,
  `LV` int(11) NOT NULL,
  `PV` int(11) NOT NULL,
  `PM` int(11) NOT NULL,
  `Attaque` int(11) NOT NULL,
  `Puissance_Magique` int(11) NOT NULL,
  `Défense` int(11) NOT NULL,
  `Résistance_Magique` int(11) NOT NULL,
  `Vitesse` int(11) NOT NULL,
  `Golds_Give` int(11) NOT NULL,
  `XP_Give` int(11) NOT NULL,
  `id_Famille` int(11) NOT NULL,
  `sprite_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `monstres`
--

INSERT INTO `monstres` (`id`, `nom`, `LV`, `PV`, `PM`, `Attaque`, `Puissance_Magique`, `Défense`, `Résistance_Magique`, `Vitesse`, `Golds_Give`, `XP_Give`, `id_Famille`, `sprite_name`) VALUES
(1, 'Soldat Squelette', 10, 35, 35, 17, 21, 23, 15, 14, 270, 12, 2, 'NONE'),
(2, 'Gluant', 1, 6, 2, 4, 3, 3, 1, 5, 3, 3, 1, 'NONE');

-- --------------------------------------------------------

--
-- Structure de la table `objet`
--

CREATE TABLE `objet` (
  `id` int(11) NOT NULL,
  `nom` varchar(255) NOT NULL,
  `Description` varchar(255) DEFAULT NULL,
  `sprite_name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


INSERT INTO `objet` (`id`, `nom`, `Description`, `sprite_name`) VALUES
(1, 'Herbe médicinale', 'Rend environ 40PV.', 'NONE'),
(2, 'Remède puissant', 'Rend environ 80PV.', 'NONE'),
(3, 'Remède spécial', 'Rend environ 120PV.', 'NONE'),
(4, 'Remède supérieur', 'Rend environ 200PV.', 'NONE'),
(5, 'Herbe curative', 'Guérie tous les statuts.', 'NONE'),
(6, 'Eau magique', 'Rend environ 30PM.', 'NONE'),
(7, 'Elixir du sage', 'Rend environ 60PM.', 'NONE'),
(8, 'Élixir elfique', 'Rend environ 120PM.', 'NONE'),
(9, 'Rosée d''Yggdrasil', 'Rend environ 400PV et 250PM.', 'NONE'),
(10, 'Poudre décuplo', 'Boost l''attaque.', 'NONE'),
(11, 'Vitesse plus', 'Rend environ 40PV.', 'NONE'),
(12, 'Défense plus', 'Rend environ 40PV.', 'NONE');

-- --------------------------------------------------------

--
-- Structure de la table `résistance`
--

CREATE TABLE `résistance` (
  `id` int(11) NOT NULL,
  `id_monstre` int(11) NOT NULL,
  `id_type_résisté` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `résistance` (`id`, `id_monstre`, `id_type_résisté`) VALUES
(1, 1, 1),
(2, 1, 2);

-- --------------------------------------------------------

--
-- Structure de la table `type`
--

CREATE TABLE `type` (
  `id` int(11) NOT NULL,
  `nom` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `type`
--

INSERT INTO `type` (`id`, `nom`) VALUES
(1, 'feu'),
(2, 'eau'),
(3, 'plante'),
(4, 'lumière'),
(5, 'ténèbre');

-- --------------------------------------------------------

--
-- Structure de la table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `pseudo` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `classe` varchar(255) DEFAULT NULL,
  `points_de_compétences` int(11) DEFAULT NULL,
  `LV` int(11) NOT NULL,
  `PV` int(11) NOT NULL,
  `PM` int(11) NOT NULL,
  `Attaque` int(11) NOT NULL,
  `Puissance_Magique` int(11) NOT NULL,
  `Défense` int(11) NOT NULL,
  `Résistance_Magique` int(11) NOT NULL,
  `Vitesse` int(11) NOT NULL,
  `Esquive` int(11) NOT NULL,
  `Golds` int(11) NOT NULL,
  `XP_For_Next_LV` int(11) NOT NULL,
  `XP` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `users`
--

INSERT INTO `users` (`id`, `pseudo`, `password`, `classe`, `points_de_compétences`, `LV`, `PV`, `PM`, `Attaque`, `Puissance_Magique`, `Défense`, `Résistance_Magique`, `Vitesse`, `Golds`, `XP_For_Next_LV`, `XP`) VALUES
(1, 'Reitag', 'Reitag', 'Guerrier', 25, 10, 80, 35, 28, 11, 31, 10, 27, 50150, 819, 42);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `arme`
--
ALTER TABLE `arme`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `armure`
--
ALTER TABLE `armure`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `boutique`
--
ALTER TABLE `boutique`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `compétences`
--
ALTER TABLE `compétences`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `compétences_apprises`
--
ALTER TABLE `compétences_apprises`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `compétences_par_arbre`
--
ALTER TABLE `compétences_par_arbre`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `compétences_par_lv`
--
ALTER TABLE `compétences_par_lv`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `equipement_users`
--
ALTER TABLE `equipement_users`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `faiblesse`
--
ALTER TABLE `faiblesse`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `inventaire`
--
ALTER TABLE `inventaire`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `loot`
--
ALTER TABLE `loot`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `monstres`
--
ALTER TABLE `monstres`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `objet`
--
ALTER TABLE `objet`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `résistance`
--
ALTER TABLE `résistance`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `type`
--
ALTER TABLE `type`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
