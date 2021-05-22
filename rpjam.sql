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
(1, 'épée en pierre', 'épée', 'Attaque', 5, 'épéepierre'),
(2, 'Sabre', 'épée', 'Attaque', 6, 'Sabre'),
(3, 'Lance', 'lance', 'Attaque', 7, 'Lance'),
(4, 'Marteau', 'marteau', 'Attaque', 8, 'Marteau'),
(5, 'Hache', 'hache', 'Attaque', 10, 'Hache'),
(6, 'épée en fer', 'épée', 'Attaque', 13, 'épéefer'),
(7, 'Baguette Pur', 'baguette', 'Puissance_Magique', 10, 'BaguettePur'),
(8, 'Arc', 'arc', 'Attaque', 15, 'Arc'),
(9, 'épée sacrée', 'épée', 'Attaque', 20, 'épéesacrée'),
(10, 'Baguette Inferno', 'baguette', 'Puissance_Magique', 20, 'BaguetteInferno'),
(11, 'épée minecraft', 'épée', 'Attaque', 25, 'épéeminecraft'),
(12, 'Dague Draconique', 'dague', 'Attaque', 30, 'DagueDraconique'),
(13, 'Baguette Démonique', 'baguette', 'Puissance_Magique', 50, 'BaguetteDémonique'),
(14, 'Excalibur', 'épée', 'Attaque', 40, 'Excalibur'),
(15, 'Hache Divine', 'hache', 'Attaque', 50, 'HacheDivine');

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
(1, 'Casque Basique', 'casque', 'Défense', 3, 'CasqueBasique'),
(2, 'Casque de Viking', 'casque', 'Défense', 5, 'CasqueViking'),
(3, 'Casque de Chevalier', 'casque', 'Défense', 7, 'CasqueChevalier'),
(4, 'Casque de Samourai', 'casque', 'Défense', 10, 'CasqueSamourai'),
(5, 'Plastron de Pierre', 'plastron', 'Défense', 5, 'PlastronPierre'),
(6, 'Plastron de Fer', 'plastron', 'Défense', 7, 'PlastronFer'),
(7, 'Plastron de Platine', 'plastron', 'Défense', 10, 'PlastronPlatine'),
(8, 'Plastron Minecraft', 'plastron', 'Défense', 15, 'PlastronMinecraft'),
(9, 'Jambières Basique', 'jambières', 'Résistance_Magique', 3, 'JambièreBasique'),
(10, 'Jambières Fer', 'jambières', 'Résistance_Magique', 5, 'JambièreFer'),
(11, 'Jambières Forte', 'jambières', 'Résistance_Magique', 7, 'JambièreForte'),
(12, 'Jambières Platine', 'jambières', 'Résistance_Magique', 10, 'JambièrePlatine'),
(13, 'Bottes en Cuir', 'bottes', 'Vitesse', 5, 'BottesCuir'),
(14, 'Bottes de Maille', 'bottes', 'Vitesse', 10, 'BottesMaille'),
(15, 'Bottes de Fer', 'bottes', 'Vitesse', 15, 'BottesFer'),
(16, 'Bottes de Platine', 'bottes', 'Vitesse', 20, 'BottesPlatine'),
(17, 'Anneau en Fer', 'anneau', 'Puissance_Magique', 5, 'AnneauFer'),
(18, 'Anneau de Platine', 'anneau', 'Puissance_Magique', 7, 'AnneauPlatine'),
(19, 'Anneau de Diamant', 'anneau', 'Puissance_Magique', 10, 'AnneauDiamant'),
(20, 'Anneau Unique', 'anneau', 'Puissance_Magique', 15, 'AnneauUnique'),
(21, 'Collier Simple', 'collier', 'Esquive', 2, 'CollierSimple'),
(22, 'Collier en Or', 'collier', 'Esquive', 3, 'CollierOr'),
(23, 'Collier de Rubis', 'collier', 'Esquive', 4, 'CollierRubis'),
(24, 'Collier en Emeraude', 'collier', 'Esquive', 5, 'CollierEmeraude');

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

INSERT INTO `boutique` VALUES
(1, 1, 'objet', 250),
(2, 2, 'objet', 500),
(3, 3, 'objet', 1000),
(4, 4, 'objet', 2000),
(5, 5, 'objet', 500),
(6, 6, 'objet', 350),
(7, 7, 'objet', 1050),
(8, 8, 'objet', 1700),
(9, 9, 'objet', 10000),
(10, 10, 'objet', 10000),
(11, 11, 'objet', 10000),
(12, 12, 'objet', 10000),
(13, 1, 'arme', 500),
(14, 2, 'arme', 600),
(15, 3, 'arme', 800),
(16, 4, 'arme', 1000),
(17, 5, 'arme', 1500),
(18, 6, 'arme', 2500),
(19, 7, 'arme', 2000),
(20, 8, 'arme', 5000),
(21, 9, 'arme', 10000),
(22, 10, 'arme', 10000),
(23, 11, 'arme', 18000),
(24, 12, 'arme', 27000),
(25, 13, 'arme', 50000),
(26, 14, 'arme', 35000),
(27, 15, 'arme', 50000),
(28, 1, 'armure', 500),
(29, 2, 'armure', 4000),
(30, 3, 'armure', 10000),
(31, 4, 'armure', 30000),
(32, 5, 'armure', 500),
(33, 6, 'armure', 4000),
(34, 7, 'armure', 10000),
(35, 8, 'armure', 30000),
(36, 9, 'armure', 500),
(37, 10, 'armure', 4000),
(38, 11, 'armure', 10000),
(39, 12, 'armure', 30000),
(40, 13, 'armure', 500),
(41, 14, 'armure', 4000),
(42, 15, 'armure', 10000),
(43, 16, 'armure', 30000),
(44, 17, 'armure', 500),
(45, 18, 'armure', 4000),
(46, 19, 'armure', 10000),
(47, 20, 'armure', 30000),
(48, 21, 'armure', 500),
(49, 22, 'armure', 4000),
(50, 23, 'armure', 10000),
(51, 24, 'armure', 30000);

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
(59, 1, 59);

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

INSERT INTO equipement_users VALUES
(1, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

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
(1, 4, 3),
(2, 8, 1),
(3, 10, 1),
(4, 11, 2),
(5, 13, 1),
(6, 15, 5),
(7, 16, 4),
(8, 18, 1),
(9, 22, 4),
(10, 26, 1),
(11, 33, 3),
(12, 45, 1),
(13, 46, 2),
(14, 48, 4);

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
(4, 'Démon'),
(5, 'Naturel'),
(6, 'Bête'),
(7, 'Matière');

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
(1, 1, 'objet', 1, 10),
(2, 2, 'arme', 1, 10),
(3, 3, 'armure', 1, 10),
(4, 4, 'arme', 1, 5),
(5, 4, 'armure', 1, 5),
(6, 5, 'objet', 2, 5),
(7, 5, 'objet', 6, 5),
(8, 6, 'arme', 2, 10),
(9, 7, 'armure', 5, 5),
(10, 8, 'armure', 9, 10),
(11, 9, 'arme', 3, 10),
(12, 10, 'armure', 13, 10),
(13, 11, 'objet', 2, 10),
(14, 11, 'arme', 17, 10),
(15, 12, 'objet', 2, 10),
(16, 13, 'objet', 7, 10),
(17, 14, 'arme', 23, 10),
(18, 15, 'arme', 4, 10),
(19, 16, 'objet', 2, 10),
(20, 17, 'armure', 6, 5),
(21, 18, 'armure', 2, 10),
(22, 19, 'arme', 5, 5),
(23, 20, 'objet', 7, 5),
(24, 21, 'objet', 2, 10),
(25, 22, 'arme', 7, 5),
(26, 23, 'objet', 1, 20),
(27, 24, 'objet', 2, 10),
(28, 25, 'armure', 10, 5),
(29, 25, 'armure', 14, 5),
(30, 25, 'armure', 18, 5),
(31, 25, 'armure', 22, 5),
(32, 26, 'arme', 6, 8),
(33, 27, 'objet', 2, 15),
(34, 28, 'objet', 3, 5),
(35, 29, 'armure', 3, 5),
(36, 30, 'arme', 8, 5),
(37, 31, 'armure', 7, 5),
(38, 32, 'objet', 3, 5),
(39, 33, 'objet', 8, 5),
(40, 34, 'armure', 23, 5),
(41, 35, 'arme', 9, 5),
(42, 35, 'arme', 10, 5),
(43, 36, 'armure', 11, 5),
(44, 37, 'armure', 19, 3),
(45, 38, 'objet', 4, 5),
(46, 38, 'objet', 8, 10),
(47, 39, 'armure', 15, 5),
(48, 40, 'arme', 11, 5),
(49, 41, 'objet', 9, 2),
(50, 42, 'armure', 19, 5),
(51, 43, 'arme', 12, 5),
(52, 44, 'objet', 10, 3),
(53, 45, 'armure', 23, 5),
(54, 46, 'objet', 10, 3),
(55, 47, 'objet', 11, 3),
(56, 48, 'objet', 12, 3),
(57, 49, 'objet', 9, 10),
(58, 50, 'arme', 14, 5),
(59, 51, 'armure', 4, 1),
(60, 51, 'armure', 8, 1),
(61, 51, 'armure', 12, 1),
(62, 51, 'armure', 16, 1),
(63, 51, 'armure', 20, 1),
(64, 51, 'armure', 24, 1),
(65, 52, 'arme', 13, 1),
(66, 52, 'arme', 15, 1);

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
(1, 'Gluant', 1, 15, 2, 12, 3, 3, 1, 5, 5, 3, 1, 'Gluant'),
(2, 'Gluante', 2, 18, 7, 16, 15, 7, 7, 9, 8, 4, 1, 'Gluante'),
(3, 'Fantôme', 3, 21, 16, 19, 18, 11, 11, 13, 15, 5, 2, 'Fantome'),
(4, 'Médigluant', 4, 25, 25, 22, 23, 15, 15, 17, 21, 8, 1, 'Médigluant'),
(5, 'Vampivol', 5, 27, 29, 26, 27, 19, 19, 21, 29, 11, 4, 'Vampivol'),
(6, 'Faune', 6, 30, 33, 28, 27, 23, 23, 25, 36, 15, 6, 'Faune'),
(7, 'Ornitoxe', 7, 35, 36, 30, 29, 27, 27, 29, 46, 22, 6, 'Ornitoxe'),
(8, 'Souche Zombie', 8, 36, 41, 34, 35, 31, 31, 33, 51, 28, 2, 'SoucheZombie'),
(9, 'Smilodon de Lait', 9, 38, 42, 36, 35, 35, 35, 37, 53, 37, 6, 'SmilodonDeLait'),
(10, 'Sac à Trésor', 10, 40, 46, 39, 40, 39, 39, 41, 59, 51, 7, 'SacATrésor'),
(11, 'BrûleFlamme', 11, 42, 50, 42, 43, 41, 41, 45, 64, 66, 7, 'BruleFlamme'),
(12, 'Main de Boue', 12, 45, 52, 46, 45, 45, 45, 49, 67, 86, 5, 'MainDeBoue'),
(13, 'Momie', 13, 46, 58, 48, 47, 49, 49, 49, 73, 120, 2, 'Momie'),
(14, 'SabreTueur', 14, 48, 61, 51, 50, 53, 53, 53, 77, 167, 7, 'SabreTueur'),
(15, 'Trode', 15, 50, 62, 53, 54, 57, 57, 57, 83, 217, 5, 'Trode'),
(16, 'Chevalier Zombie', 16, 52, 64, 56, 55, 61, 61, 61, 91, 282, 2, 'ChevalierZombie'),
(17, 'VampiGluant', 17, 56, 68, 58, 59, 65, 65, 65, 99, 366, 1, 'VampiGluant'),
(18, 'Grocha', 18, 58, 71, 60, 59, 69, 69, 69, 104, 476, 6, 'Grocha'),
(19, 'Gremlins', 19, 61, 73, 62, 61, 73, 73, 73, 107, 620, 6, 'Gremlins'),
(20, 'Dragronce', 20, 63, 75, 64, 61, 77, 77, 77, 111, 806, 3, 'Dragronce'),
(21, 'Gluant Translucide', 21, 66, 78, 68, 69, 81, 81, 81, 118, 1209, 1, 'GluantTranslucide'),
(22, 'Démon Inférieur', 22, 68, 81, 73, 72, 85, 85, 85, 121, 1813, 4, 'DémonInférieur'),
(23, 'Gigluant', 23, 73, 83, 76, 75, 89, 89, 89, 125, 2720, 1, 'Gigluant'),
(24, 'Meno Macho', 24, 74, 87, 78, 77, 93, 93, 93, 130, 4080, 6, 'MenoMacho'),
(25, 'Sorcier', 25, 76, 89, 81, 82, 97, 97, 97, 133, 6120, 4, 'Sorcier'),
(26, 'Frelon Tueur', 26, 79, 92, 83, 82, 101, 101, 101, 138, 9180, 5, 'FrelonTueur'),
(27, 'Dragon Vert', 27, 81, 96, 86, 85, 105, 105, 105, 142, 13771, 3, 'DragonVert'),
(28, 'Roi Gluant', 28, 84, 98, 88, 85, 109, 109, 109, 148, 20656, 1, 'RoiGluant'),
(29, 'Vercule', 29, 86, 101, 91, 85, 113, 113, 113, 151, 30985, 6, 'Vercule'),
(30, 'Phalène Tueuse', 30, 89, 104, 93, 90, 117, 117, 117, 156, 46478, 6, 'PhalèneTueuse'),
(31, 'Troll', 31, 90, 106, 94, 93, 121, 121, 121, 160, 69717, 5, 'Troll'),
(32, 'GronnOeil', 32, 93, 109, 96, 97, 125, 125, 125, 167, 104575, 7, 'GronnOeil'),
(33, 'Gracos', 33, 97, 113, 99, 98, 129, 129, 129, 172, 156863, 5, 'Gracos'),
(34, 'Shivattak', 34, 99, 117, 102, 101, 133, 133, 133, 176, 235294, 4, 'Shivattak'),
(35, 'Roi Gluant de Métal', 35, 101, 121, 106, 105, 137, 137, 137, 183, 352942, 1, 'RoiGluantMétal'),
(36, 'Incarnus', 36, 104, 124, 107, 108, 141, 141, 141, 186, 529413, 6, 'Incarnus'),
(37, 'Bastonnier', 37, 106, 128, 109, 108, 145, 145, 145, 192, 794120, 6, 'Bastonnier'),
(38, 'Géant', 38, 109, 131, 111, 110, 149, 149, 149, 200, 1191180, 6, 'Géant'),
(39, 'Phix', 39, 113, 135, 114, 113, 153, 153, 153, 208, 1786000, 7, 'Phix'),
(40, 'Roi Serpent', 40, 119, 138, 116, 115, 157, 157, 157, 214, 2680155, 6, 'RoiSerpent'),
(41, 'Gluant d''Or', 41, 121, 142, 119, 120, 161, 161, 161, 219, 4020232, 1, 'GluantOr'),
(42, 'Grand Dragon', 42, 125, 143, 122, 121, 165, 165, 165, 225, 6030348, 3, 'GrandDragon'),
(43, 'Psaro', 43, 127, 147, 124, 123, 169, 169, 169, 239, 7839453, 2, 'Psaro'),
(44, 'Chef Troll', 44, 130, 150, 126, 125, 173, 173, 173, 246, 10191289, 5, 'ChefTroll'),
(45, 'Dragon Poison', 45, 134, 153, 129, 128, 177, 177, 177, 258, 15286934, 3, 'DragonPoison'),
(46, 'Dragon Flamboyant', 46, 136, 158, 132, 131, 181, 181, 181, 304, 22930401, 3, 'DragonFlamboyant'),
(47, 'Machine à Exterminer', 47, 139, 163, 136, 135, 185, 185, 185, 309, 34395601, 7, 'MachineAExterminer'),
(48, 'Ange Déchu', 48, 143, 168, 138, 139, 189, 189, 189, 319, 51593402, 4, 'AngeDéchu'),
(49, 'LordDraco', 49, 149, 169, 141, 140, 193, 193, 193, 343, 77390103, 3, 'LordDraco'),
(50, 'Seigneur Dragovien', 50, 152, 170, 143, 142, 197, 197, 197, 349, 100607134, 3, 'SeigneurDragovien'),
(51, 'Yamete', 51, 156, 175, 146, 150, 201, 201, 201, 369, 130789275, 4, 'Yamete'),
(52, 'Léviantan', 52, 160, 180, 150, 153, 210, 210, 210, 400, 170026058, 3, 'Léviantan');


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
(1, 'Herbe médicinale', 'Rend environ 40PV.', 'HerbeMédicinale'),
(2, 'Remède puissant', 'Rend environ 80PV.', 'RemèdePuissant'),
(3, 'Remède spécial', 'Rend environ 120PV.', 'RemèdeSpécial'),
(4, 'Remède supérieur', 'Rend environ 200PV.', 'RemèdeSupérieur'),
(5, 'Herbe curative', 'Guérie tous les statuts.', 'HerbeCurative'),
(6, 'Eau magique', 'Rend environ 30PM.', 'EauMagique'),
(7, 'Elixir du sage', 'Rend environ 60PM.', 'ElixirDuSage'),
(8, 'Élixir elfique', 'Rend environ 120PM.', 'ÉlixirElfique'),
(9, 'Rosée d''Yggdrasil', 'Rend environ 400PV et 250PM.', 'RoséeYggdrasil'),
(10, 'Poudre décuplo', 'Boost l''attaque.', 'PoudreDécuplo'),
(11, 'Vitesse plus', 'Boost la vitesse.', 'VitessePlus'),
(12, 'Défense plus', 'Boost la défense.', 'Défenseplus');

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
(1, 3, 1),
(2, 4, 1),
(3, 5, 5),
(4, 8, 3),
(5, 11, 1),
(6, 12, 2),
(7, 15, 1),
(8, 15, 2),
(9, 15, 3),
(10, 16, 5),
(11, 21, 4),
(12, 22, 1),
(13, 25, 1),
(14, 25, 2),
(15, 25, 3),
(16, 28, 1),
(17, 31, 3),
(18, 35, 1),
(19, 35, 2),
(20, 35, 3),
(21, 35, 4),
(22, 35, 5),
(23, 36, 4),
(24, 38, 2),
(25, 39, 3),
(26, 41, 1),
(27, 41, 4),
(28, 42, 4),
(29, 42, 5),
(30, 44, 3),
(31, 45, 3),
(32, 46, 1),
(33, 48, 5),
(34, 51, 1),
(35, 51, 2),
(36, 51, 3),
(37, 51, 4),
(38, 51, 5),
(39, 52, 5);

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
(1, 'Reitag', '863258b32fe932c8717c29182b5ee7e3', 'Guerrier', 28, 12, 86, 40, 36, 14, 36, 13, 31, 0, 53660, 1844, 36);

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
