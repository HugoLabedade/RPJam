-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : jeu. 13 mai 2021 à 15:47
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

--
-- Déchargement des données de la table `arme`
--

INSERT INTO `arme` (`id`, `nom`, `type_arme`, `stat_boost`, `bonus_stat`, `sprite_name`) VALUES
(1, 'arme_test', 'épée', 'Attaque', 15, NULL);

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

--
-- Déchargement des données de la table `armure`
--

INSERT INTO `armure` (`id`, `nom`, `type_armure`, `stat_boost`, `bonus_stat`, `sprite_name`) VALUES
(1, 'armure_test', 'casque', 'Attaque', 15, NULL);

-- --------------------------------------------------------

--
-- Structure de la table `boutique`
--

CREATE TABLE `boutique` (
  `id` int(11) NOT NULL,
  `id_item` int(11) NOT NULL,
  `table_item` varchar(255) NOT NULL,
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
  `Autres` tinyint(1) DEFAULT NULL,
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
(1, 'Lame de feu', 20, 'Physique', 0, NULL, '1', 10, 'Fend l''ennemi avec une épée incandescente.', 1, 5),
(2, 'Lame du dragon', 30, 'Physique', 0, 3, NULL, NULL, 'Attaque qui inflige d''importants dégâts aux dragons.', NULL, 5),
(3, 'Lame de métal', 10, 'Physique', 0, 4, NULL, NULL, 'Attaque qui endommage même les ennemis métalliques.', NULL, 5),
(4, 'Coup miraculeux', 45, 'Physique', 1, NULL, NULL, NULL, 'Attaque mystérieuse qui inflige des dégâts à l''ennemi tout en guérissant les blessures de l''utilisateur.', NULL, 25),
(5, 'Attaque du faucon', 70, 'Physique', 0, NULL, NULL, NULL, 'Inflige une attaque de taille plus rapide qu''un faucon en vol.', NULL, 25),
(6, 'Gigentaille', 100, 'Physique', 0, NULL, NULL, NULL, 'Technique d''épée secrète à une main qui foudroie tous les ennemis par de violents éclairs.', NULL, 35),
(7, 'Lame ultime', 150, 'Physique', 0, NULL, NULL, NULL, 'Fend l''ennemi avec une épée incandescente.', NULL, 45),
(8, 'Soin Léger', NULL, NULL, 1, NULL, NULL, NULL, 'Rend une partie des PV à d''un allié.', NULL, 8),
(9, 'Soin Partiel', NULL, NULL, 1, NULL, NULL, NULL, 'Rend la moitié des PV à d''un allié.', NULL, 20),
(10, 'Soin Complet', NULL, NULL, 1, NULL, NULL, NULL, 'Rend tous les PV à un allié.', NULL, 45),
(11, 'Somnifer', 15, 'Physique', 0, NULL, '3', 40, 'Poignarde un ennemi de telle manière que celui-ci s''endort parfois.', NULL, 6),
(12, 'Persécutter', 10, 'Physique', 1, NULL, NULL, NULL, 'Coup sournois qui multiplie parfois par six les dégâts infligés aux ennemis endormis ou désorientés.', NULL, 11),
(13, 'Morsure du cobra', 15, 'Physique', 0, NULL, '4', 40, 'Poignarde un ennemi de telle manière que celui-ci est parfois intoxiqué.', NULL, 6),
(14, 'Coupe franche', 10, 'Physique', 1, NULL, NULL, NULL, 'Coup sournois qui multiplie parfois par six les dégâts infligés aux ennemis empoisonnés ou paralysés.', NULL, 11),
(15, 'Esquiveur', NULL, NULL, 1, NULL, NULL, NULL, 'Pas de danse qui augmente la capacité de l''utilisateur d''esquiver les attaques.', NULL, 10),
(16, 'Critique systématique', 10, 'Physique', 0, NULL, NULL, NULL, 'Aptitude incroyable qui garantie de placer un coup critique sur l''ennemi.', NULL, 35),
(17, 'Lucifroid', 20, 'Magique', 0, 5, '5', 25, 'Attaque qui peut infliger de gros dégâts aux démons et qui les paralyse parfois par la même occasion.', NULL, 7),
(18, 'Aura de peur', NULL, NULL, 1, NULL, NULL, NULL, 'Réduit la résistance de l''ennemi à tous les sorts offensifs.', NULL, 15),
(19, 'Souffle du sage', NULL, NULL, 1, NULL, NULL, NULL, 'Lève un vent surnaturel qui rend peu à peu ses PM à l''utilisateur.', NULL, 10),
(20, 'Psychocanalisation', NULL, NULL, 0, NULL, NULL, NULL, 'Augmente fortement les dégâts infligés par n''importe quel sort offensif lancé par l''utilisateur.', NULL, 20),
(21, 'Flamme', 15, 'Magique', 0, NULL, '1', 5, 'Lance une flamme sur un ennemi', 1, 10),
(22, 'Superflamme', 40, 'Magique', 0, NULL, '1', 10, 'Lance une boule de feu sur un ennemi', 1, 30),
(23, 'Gigaflamme', 100, 'Magique', 0, NULL, '1', 20, 'Anéanti un seul ennemi avec une boule de feu gigantesque.', 1, 75),
(24, 'Clic-clac-zap', NULL, NULL, 1, NULL, NULL, NULL, 'Une gerbe d''étincelles violettes protège un membre de l''équipe des altérations d''état.', NULL, 20),
(25, 'Grâce de la Déesse', NULL, NULL, 1, NULL, NULL, NULL, 'Bienheureuse bénédiction qui ressuscite l''utilisateur s''il lui arrive malheur.', NULL, 150),
(26, 'Coup bestial', 15, 'Physique', 0, 7, NULL, NULL, 'Coup qui inflige de gros dégâts aux monstres de la famille des bêtes.', NULL, 7),
(27, 'Délivrance', 20, 'Physique', 0, 2, NULL, NULL, 'Coup de lance sacrée qui peut infliger de gros dégâts aux morts-vivants.', NULL, 10),
(28, 'Tonnerre divin', 70, 'Magique', 1, NULL, NULL, NULL, 'Cette compétence lumineuse anéanti l''ennemi avec un puissant élair, elle possède un fort taux de coup critique.', 4, 50),
(29, 'Ball''ombre', 120, 'Magique', 0, NULL, '3', NULL, 'Lance une masse d''énergie noir sur l''ennemi, peut parfois l''endormir.', 5, 100),
(30, 'Cercle du carnage', NULL, NULL, 1, NULL, NULL, NULL, 'Invoque un sceau qui augmente les chances d''infliger des sorts critiques.', NULL, 7),
(31, 'Hypnolame', 10, 'Physique', 0, NULL, '2', 15, 'Attaque à l''épée qui peut parfois désorienter l''ennemi.', NULL, 7),
(32, 'Flagellan', 20, 'Physique', 0, NULL, '3', 25, 'Attaque à l''épée placée sur un ennemi et qui peut parfois l''endormir.', NULL, 10),
(33, 'Foudre', 20, 'Magique', 0, NULL, NULL, NULL, 'Petit éclair qui inflige des dommages à l''ennemi.', 4, 10),
(34, 'Superfoudre', 50, 'Magique', 0, NULL, '5', 10, 'Éclair puissant qui peut parfois paralyser l''ennemi.', 4, 30),
(35, 'Gigafoudre', 90, 'Magique', 0, NULL, '5', 25, 'Anéanti l''ennemi avec un éclair surpuissant, peut paralyser l''ennemi.', 4, 75),
(36, 'Glace', 20, 'Magique', 0, NULL, NULL, NULL, 'Pilone de glace envpyer sur l''ennemi.', 2, 10),
(37, 'Superglace', 60, 'Magique', 0, NULL, NULL, NULL, 'Gros bloc de glace envoyer sur l''ennemi.', 2, 25),
(38, 'Gigaglace', 100, 'Magique', 0, NULL, NULL, NULL, 'Lance un énorme bloc de glace sur l''ennemi.', 2, 65),
(39, 'Tornade', 20, 'Magique', 0, NULL, NULL, NULL, 'Lance une brise qui blesse l''ennemi.', NULL, 12),
(40, 'Supertornade', 50, 'Magique', 0, NULL, '2', 10, 'Lance une bourasque qui peut parfois désorienter l''ennemi.', NULL, 30),
(41, 'Gigatornade', 80, 'Magique', 0, NULL, '2', 25, 'Lance une immense tornade que peut désorienter l''ennemi.', NULL, 65),
(42, 'Tranch''herbe', 40, 'Magique', 0, NULL, NULL, NULL, 'Lance des feuilles coupantes sur l''ennemi.', 3, 25),
(43, 'Tempête Verte', 85, 'Magique', 0, NULL, NULL, NULL, 'Lance une tempête de feuilles coupantes sur l''ennemi', 3, 60),
(44, 'Toxic', NULL, NULL, 0, NULL, '4', 100, 'Empoisoner l''ennemi.', NULL, 25),
(45, 'Onde folie', NULL, NULL, 0, NULL, '2', 100, 'Désorienter l''ennemi.', NULL, 25),
(46, 'Feu follet', NULL, NULL, 0, NULL, '1', 100, 'Brûler l''ennemi.', NULL, 25),
(47, 'Hypnose', NULL, NULL, 0, NULL, '3', 100, 'Endormir l''ennemi.', NULL, 25),
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
(59, 'Hâte', NULL, NULL, 1, NULL, NULL, NULL, 'Boost la vitesse de l''utilisateur.', NULL, 15);

-- --------------------------------------------------------

--
-- Structure de la table `compétences_apprises`
--

CREATE TABLE `compétences_apprises` (
  `id` int(11) NOT NULL,
  `id_Users` int(11) NOT NULL,
  `id_compétences` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `compétences_apprises`
--

INSERT INTO `compétences_apprises` (`id`, `id_Users`, `id_compétences`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 3),
(4, 1, 4),
(5, 1, 5),
(6, 1, 6),
(7, 1, 7),
(8, 1, 8),
(9, 1, 9),
(10, 1, 10),
(11, 1, 11),
(12, 1, 12),
(13, 1, 13),
(14, 1, 14),
(15, 1, 15),
(16, 1, 16),
(17, 1, 17),
(18, 1, 18),
(19, 1, 19),
(20, 1, 20),
(21, 1, 21),
(22, 1, 22),
(23, 1, 23),
(24, 1, 24),
(25, 1, 25),
(26, 1, 26),
(27, 1, 27),
(28, 1, 28),
(29, 1, 29),
(30, 1, 30),
(31, 1, 31),
(32, 1, 32),
(33, 1, 33),
(34, 1, 34),
(35, 1, 35),
(36, 1, 36),
(37, 1, 37),
(38, 1, 38),
(39, 1, 39),
(40, 1, 40),
(41, 1, 41),
(42, 1, 42),
(43, 1, 43),
(44, 1, 44),
(45, 1, 45),
(46, 1, 46),
(47, 1, 47),
(48, 1, 48),
(49, 1, 49),
(50, 1, 50),
(51, 1, 51),
(52, 1, 52),
(53, 1, 53),
(54, 1, 54),
(55, 1, 55),
(56, 1, 56),
(57, 1, 57),
(58, 1, 58),
(59, 1, 59),
(60, 1, 60);

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


INSERT INTO `compétences_par_lv` (`id`, `classe`, `id_compétences`, `LV_Obtention`) VALUES
(1, 'Guerrier', 1, 5),
(2, 'Guerrier', 2, 9),
(3, 'Guerrier', 5, 15),
(4, 'Guerrier', 21, 17),
(5, 'Guerrier', 22, 20),
(6, 'Guerrier', 48, 26),
(7, 'Guerrier', 26, 31),
(8, 'Guerrier', 27, 37),
(9, 'Guerrier', 59, 40),
(10, 'Assassin', 11, 5),
(11, 'Assassin', 12, 9),
(12, 'Assassin', 13, 14),
(13, 'Assassin', 14, 18),
(14, 'Assassin', 32, 21),
(15, 'Assassin', 31, 26),
(16, 'Assassin', 1, 29),
(17, 'Assassin', 2, 34),
(18, 'Assassin', 44, 36),
(19, 'Assassin', 47, 40),
(20, 'Mage', 21, 5),
(21, 'Mage', 17, 9),
(22, 'Mage', 39, 12),
(23, 'Mage', 8, 16),
(24, 'Mage', 22, 19),
(25, 'Mage', 58, 25),
(26, 'Mage', 40, 27),
(27, 'Mage', 9, 30),
(28, 'Mage', 44, 31),
(29, 'Mage', 47, 32),
(30, 'Mage', 23, 36),
(31, 'Mage', 41, 38),
(32, 'Mage', 10, 40);

-- --------------------------------------------------------

--
-- Structure de la table `effet`
--

CREATE TABLE `effet` (
  `id` int(11) NOT NULL,
  `Effet` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `effet`
--

INSERT INTO `effet` (`id`, `Effet`) VALUES
(1, 'Brûlure'),
(2, 'Confusion'),
(3, 'Sommeil'),
(4, 'Poison'),
(5, 'Paralysie');

-- --------------------------------------------------------

--
-- Structure de la table `equipement_users`
--

CREATE TABLE `equipement_users` (
  `id_Users` int(11) NOT NULL,
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

--
-- Déchargement des données de la table `faiblesse`
--

INSERT INTO `faiblesse` (`id`, `id_monstre`, `id_type_faiblesse`) VALUES
(1, 1, 4),
(2, 1, 5);

-- --------------------------------------------------------

--
-- Structure de la table `famille`
--

CREATE TABLE `famille` (
  `id` int(11) NOT NULL,
  `nom` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `famille`
--

INSERT INTO `famille` (`id`, `nom`) VALUES
(1, 'Gluant'),
(2, 'Zombie'),
(3, 'Dragon'),
(4, 'Métal'),
(5, 'Démon'),
(6, 'Naturel'),
(7, 'Bête'),
(8, 'Matière');

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

--
-- Déchargement des données de la table `inventaire`
--

INSERT INTO `inventaire` (`id`, `id_Users`, `id_item`, `quantité`) VALUES
(1, 1, 1, 9),
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

-- --------------------------------------------------------

--
-- Structure de la table `inventaire_armes`
--

CREATE TABLE `inventaire_armes` (
  `id` int(11) NOT NULL,
  `id_Users` int(11) NOT NULL,
  `id_item` int(11) NOT NULL,
  `quantité` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `inventaire_armes`
--

INSERT INTO `inventaire_armes` (`id`, `id_Users`, `id_item`, `quantité`) VALUES
(1, 1, 1, 5);

-- --------------------------------------------------------

--
-- Structure de la table `inventaire_armures`
--

CREATE TABLE `inventaire_armures` (
  `id` int(11) NOT NULL,
  `id_Users` int(11) NOT NULL,
  `id_item` int(11) NOT NULL,
  `quantité` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `inventaire_armures`
--

INSERT INTO `inventaire_armures` (`id`, `id_Users`, `id_item`, `quantité`) VALUES
(1, 1, 1, 2);

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

--
-- Déchargement des données de la table `loot`
--

INSERT INTO `loot` (`id`, `id_monstre`, `table_du_loot`, `id_loot`, `pourcentage_loot`) VALUES
(1, 1, 'arme', 1, 10),
(2, 1, 'armure', 1, 5),
(3, 1, 'objet', 1, 20);

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
(2, 'Gluant', 1, 6, 2, 4, 3, 3, 1, 5, 3, 3, 1, 'NONE'),
(3, 'Pour les test', 1, 250, 250, 30, 30, 30, 30, 30, 0, 0, 0, 'NONE');

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

--
-- Déchargement des données de la table `objet`
--

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
(11, 'Vitesse plus', 'Boost la vitesse.', 'NONE'),
(12, 'Défense plus', 'Boost la défense.', 'NONE');

-- --------------------------------------------------------

--
-- Structure de la table `résistance`
--

CREATE TABLE `résistance` (
  `id` int(11) NOT NULL,
  `id_monstre` int(11) NOT NULL,
  `id_type_résisté` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `résistance`
--

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

INSERT INTO `users` (`id`, `pseudo`, `password`, `classe`, `points_de_compétences`, `LV`, `PV`, `PM`, `Attaque`, `Puissance_Magique`, `Défense`, `Résistance_Magique`, `Vitesse`, `Esquive`, `Golds`, `XP_For_Next_LV`, `XP`) VALUES
(1, 'Reitag', 'Reitag', 'Guerrier', 28, 12, 86, 40, 36, 14, 36, 13, 31, 0, 53660, 1844, 36);

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
  ADD PRIMARY KEY (`id_Users`);

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
