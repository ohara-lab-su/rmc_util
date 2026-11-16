# 実装に基づく API 索引

このページは、提供された Python ソースの定義を基に作成した索引です。関数名・クラス名は実装から取得しています。**公開 API の保証を示すものではありません。** 実際の利用手順は [README ベースのマニュアル](../guide/readme_manual.md) を参照してください。

## [`config`](config.md)

対象ソース: `config(20261116-081311).py`

- クラス `Config`（定義行 13）
  - `__init__()`（定義行 88）
  - `load_yaml()`（定義行 107）

## [`install`](install.md)

対象ソース: `install.py`

- 関数 `find_installed_scripts()`（定義行 19）
- 関数 `install_scripts()`（定義行 41）
- 関数 `main()`（定義行 76）

## [`rmc_pot`](rmc_pot.md)

対象ソース: `rmc_pot(20261116-081310).py`

- クラス `RmcPot`（定義行 28）
  - `__init__()`（定義行 34）
  - `rmc_dat()`（定義行 114）
  - `set_cfg_name()`（定義行 117）
  - `set_tag()`（定義行 132）
  - `get_tag()`（定義行 148）
  - `init()`（定義行 167）
  - `preprocess()`（定義行 181）
  - `postprocess()`（定義行 261）
  - `check_fnc_cutoff_consistency()`（定義行 342）
  - `run()`（定義行 729）
  - `ensure_vasp5_format()`（定義行 839）
  - `cfg2poscar()`（定義行 863）

## [`rmc_pot_dat`](rmc_pot_dat.md)

対象ソース: `rmc_pot_dat(20261116-081310).py`

- クラス `RmcPotDat`（定義行 22）
  - `__init__()`（定義行 25）
  - `set_free_format()`（定義行 55）
  - `set_cfg_name()`（定義行 71）
  - `init()`（定義行 82）
  - `is_free_format()`（定義行 155）
- 関数 `main()`（定義行 181）

## [`rmc_pot_dat_fixed`](rmc_pot_dat_fixed.md)

対象ソース: `rmc_pot_dat_fixed(10).py`

- クラス `RmcPotDatFixed`（定義行 67）
  - `__init__()`（定義行 82）
  - `set_cfg_name()`（定義行 184）
  - `create_dat_file()`（定義行 193）
  - `load()`（定義行 260）
  - `write()`（定義行 292）
  - `get_line()`（定義行 311）
  - `set_line()`（定義行 325）
  - `insert_line()`（定義行 355）
  - `remove_line()`（定義行 379）
  - `set_element_info()`（定義行 444）
  - `get_comment()`（定義行 460）
  - `set_comment()`（定義行 464）
  - `get_density()`（定義行 475）
  - `set_density()`（定義行 500）
  - `get_cutoffs()`（定義行 511）
  - `set_cutoffs()`（定義行 530）
  - `get_max_moves()`（定義行 613）
  - `set_maximum_moves()`（定義行 631）
  - `get_r_spacing()`（定義行 660）
  - `set_r_spacing()`（定義行 688）
  - `get_moveout_option()`（定義行 699）
  - `set_moveout_option()`（定義行 745）
  - `get_num_config_to_collect()`（定義行 781）
  - `set_num_config_to_collect()`（定義行 822）
  - `get_print_interval()`（定義行 860）
  - `set_print_interval()`（定義行 896）
  - `get_time_and_save()`（定義行 927）
  - `set_time_and_save()`（定義行 964）
  - `get_data_flags()`（定義行 1010）
  - `set_data_flags()`（定義行 1051）
  - `get_exp_filename()`（定義行 1098）
  - `set_exp_filename()`（定義行 1160）
  - `get_exp_range()`（定義行 1193）
  - `set_exp_range()`（定義行 1239）
  - `get_scale_factor()`（定義行 1270）
  - `set_scale_factor()`（定義行 1284）
  - `get_sigma_factor()`（定義行 1299）
  - `set_sigma_factor()`（定義行 1327）
  - `get_flag_15()`（定義行 1343）
  - `set_flag_15()`（定義行 1356）
  - `get_flag_16()`（定義行 1365）
  - `set_flag_16()`（定義行 1378）
  - `get_flag_17()`（定義行 1387）
  - `set_flag_17()`（定義行 1400）
  - `get_flag_18()`（定義行 1409）
  - `set_flag_18()`（定義行 1422）
  - `get_angle_constraint_count()`（定義行 1431）
  - `set_angle_constraint_count()`（定義行 1444）
  - `get_coord_constraint_count()`（定義行 1453）
  - `set_coord_constraint_count()`（定義行 1466）
  - `get_avg_coord_constraint_count()`（定義行 1475）
  - `set_avg_coord_constraint_count()`（定義行 1488）
  - `get_potential_flag()`（定義行 1497）
  - `set_potential_flag()`（定義行 1510）
  - `get_fnc_switch()`（定義行 1519）
  - `get_fnc_options()`（定義行 1535）
  - `set_fnc_switch()`（定義行 1580）
  - `get_fnc_distance_ranges()`（定義行 1654）
  - `set_fnc_distance_ranges()`（定義行 1705）
  - `get_initial_bin_shift()`（定義行 1776）
  - `set_initial_bin_shift()`（定義行 1789）
  - `get_xmax_used()`（定義行 1798）
  - `set_xmax_used()`（定義行 1811）
  - `get_num_atoms_per_move()`（定義行 1820）
  - `set_num_atoms_per_move()`（定義行 1843）
  - `get_history_buffer_size()`（定義行 1853）
  - `set_history_buffer_size()`（定義行 1866）
  - `get_display_update_interval()`（定義行 1875）
  - `set_display_update_interval()`（定義行 1884）
  - `get_custom_move_flag()`（定義行 1893）
  - `set_custom_move_flag()`（定義行 1902）
  - `get_load_histogram_flag()`（定義行 1911）
  - `set_load_histogram_flag()`（定義行 1920）
  - `get_max_atoms_per_cell()`（定義行 1929）
  - `set_max_atoms_per_cell()`（定義行 1938）
  - `get_swap_settings()`（定義行 1947）
  - `set_swap_settings()`（定義行 1959）
  - `get_thread_count()`（定義行 1969）
  - `set_thread_count()`（定義行 1978）
  - `get_local_invariance()`（定義行 1987）
  - `set_local_invariance()`（定義行 2002）
  - `get_non_periodic()`（定義行 2026）
  - `set_non_periodic()`（定義行 2040）
  - `get_vibrational_amplitudes()`（定義行 2057）
  - `set_vibrational_amplitudes()`（定義行 2064）
- 関数 `main()`（定義行 2103）

## [`rmc_pot_dat_fnc`](rmc_pot_dat_fnc.md)

対象ソース: `rmc_pot_dat_fnc(10).py`

- クラス `FncNeighbour`（定義行 19）
- クラス `RmcPotDatFnc`（定義行 31）
  - `__init__()`（定義行 39）
  - `path()`（定義行 84）
  - `initialize()`（定義行 92）
  - `load()`（定義行 116）
  - `write()`（定義行 186）
  - `set_title()`（定義行 228）
  - `get_title()`（定義行 238）
  - `get_atom_count()`（定義行 246）
  - `set_distance_range()`（定義行 254）
  - `set_distance_ranges()`（定義行 282）
  - `get_distance_ranges()`（定義行 309）
  - `set_atom_neighbours()`（定義行 317）
  - `get_atom_neighbours()`（定義行 341）
  - `add_neighbour()`（定義行 353）
  - `add_pair()`（定義行 381）
  - `add_pairs()`（定義行 405）
  - `remove_pair()`（定義行 421）
  - `clear_atom_neighbours()`（定義行 444）
  - `add_template_instance()`（定義行 469）
  - `add_template_instances()`（定義行 488）
  - `add_group_complete_graph()`（定義行 507）
  - `validate()`（定義行 521）
  - `as_pairs()`（定義行 550）
- 関数 `main()`（定義行 644）

## [`rmc_pot_dat_free`](rmc_pot_dat_free.md)

対象ソース: `rmc_pot_dat_free(20261116-081310).py`

- クラス `RmcPotDatFree`（定義行 53）
  - `__init__()`（定義行 77）
  - `create_dat_file()`（定義行 174）
  - `load()`（定義行 255）
  - `write()`（定義行 313）
  - `set()`（定義行 516）
  - `add()`（定義行 536）
  - `get()`（定義行 555）
  - `get_all()`（定義行 577）
  - `initialize_sections()`（定義行 597）
  - `initialize_qn_constraints()`（定義行 637）
  - `add_section()`（定義行 652）
  - `remove_section()`（定義行 670）
  - `remove()`（定義行 689）
  - `section_count()`（定義行 705）
  - `set_cfg_name()`（定義行 716）
  - `set_element_info()`（定義行 728）
  - `get_comment()`（定義行 827）
  - `set_comment()`（定義行 831）
  - `get_density()`（定義行 844）
  - `set_density()`（定義行 858）
  - `get_cutoffs()`（定義行 871）
  - `set_cutoffs()`（定義行 893）
  - `get_max_moves()`（定義行 914）
  - `set_maximum_moves()`（定義行 925）
  - `get_r_spacing()`（定義行 938）
  - `set_r_spacing()`（定義行 943）
  - `get_moveout_option()`（定義行 952）
  - `set_moveout_option()`（定義行 957）
  - `get_num_config_to_collect()`（定義行 966）
  - `set_num_config_to_collect()`（定義行 971）
  - `get_print_interval()`（定義行 982）
  - `set_print_interval()`（定義行 987）
  - `get_time_and_save()`（定義行 998）
  - `set_time_and_save()`（定義行 1004）
  - `get_data_flags()`（定義行 1021）
  - `set_data_flags()`（定義行 1028）
  - `get_exp_filename()`（定義行 1071）
  - `set_exp_filename()`（定義行 1112）
  - `get_exp_range()`（定義行 1127）
  - `set_exp_range()`（定義行 1151）
  - `get_scale_factor()`（定義行 1170）
  - `set_scale_factor()`（定義行 1184）
  - `get_sigma_factor()`（定義行 1197）
  - `set_sigma_factor()`（定義行 1211）
  - `get_flag_15()`（定義行 1261）
  - `set_flag_15()`（定義行 1269）
  - `get_flag_16()`（定義行 1280）
  - `set_flag_16()`（定義行 1284）
  - `get_flag_17()`（定義行 1288）
  - `set_flag_17()`（定義行 1292）
  - `get_flag_18()`（定義行 1296）
  - `set_flag_18()`（定義行 1300）
  - `get_angle_constraint_count()`（定義行 1304）
  - `set_angle_constraint_count()`（定義行 1308）
  - `get_coord_constraint_count()`（定義行 1335）
  - `set_coord_constraint_count()`（定義行 1339）
  - `get_avg_coord_constraint_count()`（定義行 1366）
  - `set_avg_coord_constraint_count()`（定義行 1370）
  - `get_potential_flag()`（定義行 1399）
  - `set_potential_flag()`（定義行 1406）
  - `get_fnc_switch()`（定義行 1435）
  - `get_fnc_options()`（定義行 1471）
  - `set_fnc_switch()`（定義行 1534）
  - `validate_mode_configuration()`（定義行 1614）
  - `get_fnc_distance_ranges()`（定義行 1714）
  - `set_fnc_distance_ranges()`（定義行 1765）
  - `get_initial_bin_shift()`（定義行 1836）
  - `set_initial_bin_shift()`（定義行 1841）
  - `get_xmax_used()`（定義行 1849）
  - `set_xmax_used()`（定義行 1854）
  - `get_num_atoms_per_move()`（定義行 1860）
  - `set_num_atoms_per_move()`（定義行 1872）
  - `get_history_buffer_size()`（定義行 1896）
  - `set_history_buffer_size()`（定義行 1901）
  - `get_display_update_interval()`（定義行 1909）
  - `set_display_update_interval()`（定義行 1914）
  - `get_custom_move_flag()`（定義行 1922）
  - `set_custom_move_flag()`（定義行 1928）
  - `get_load_histogram_flag()`（定義行 1956）
  - `set_load_histogram_flag()`（定義行 1961）
  - `get_max_atoms_per_cell()`（定義行 1969）
  - `set_max_atoms_per_cell()`（定義行 1974）
  - `get_swap_settings()`（定義行 1986）
  - `set_swap_settings()`（定義行 1999）
  - `get_thread_count()`（定義行 2028）
  - `set_thread_count()`（定義行 2033）
  - `get_angle_constraints()`（定義行 2169）
  - `set_angle_constraint()`（定義行 2282）
  - `remove_angle_constraint()`（定義行 2415）
  - `clear_angle_constraints()`（定義行 2427）
  - `get_coord_constraints()`（定義行 2440）
  - `add_coord_constraint()`（定義行 2530）
  - `set_coord_constraint()`（定義行 2566）
  - `remove_coord_constraint()`（定義行 2680）
  - `clear_coord_constraints()`（定義行 2692）
  - `get_qn_constraints()`（定義行 2705）
  - `remove_qn_constraint()`（定義行 2823）
  - `add_qn_constraint()`（定義行 2840）
  - `set_qn_constraint()`（定義行 2884）
  - `clear_qn_constraints()`（定義行 3003）
  - `get_bvs_constraints()`（定義行 3018）
  - `set_bvs_constraint()`（定義行 3109）
  - `remove_bvs_constraint()`（定義行 3252）
  - `clear_bvs_constraints()`（定義行 3263）
  - `get_pair_potential_settings()`（定義行 3271）
  - `set_pair_potential()`（定義行 3338）
  - `clear_pair_potential()`（定義行 3449）
  - `write_pair_potential_file()`（定義行 3470）
  - `get_cos_constraints()`（定義行 3505）
  - `set_cos_constraint()`（定義行 3509）
  - `get_snc_constraints()`（定義行 3513）
  - `set_snc_constraint()`（定義行 3517）
  - `get_lj_potential()`（定義行 3521）
  - `set_lj_potential()`（定義行 3535）
  - `get_custom_move()`（定義行 3593）
  - `set_custom_move()`（定義行 3603）
  - `get_local_invariance()`（定義行 3625）
  - `set_local_invariance()`（定義行 3646）
  - `get_non_periodic()`（定義行 3685）
  - `set_non_periodic()`（定義行 3695）
  - `get_vibrational_amplitudes()`（定義行 3714）
  - `set_vibrational_amplitudes()`（定義行 3724）
  - `get_common_neighbor_constraints()`（定義行 3740）
  - `set_common_neighbor_constraint()`（定義行 3750）
  - `get_ann_potential_settings()`（定義行 3798）
  - `set_ann_potential()`（定義行 3802）
  - `get_aenet_settings()`（定義行 3835）
  - `set_aenet_potential()`（定義行 3923）
  - `add_aenet_potential_file()`（定義行 4038）
  - `remove_aenet_potential_file()`（定義行 4100）
  - `clear_aenet_potential()`（定義行 4150）
- 関数 `main()`（定義行 4172）

## [`rmc_pot_dat_top`](rmc_pot_dat_top.md)

対象ソース: `rmc_pot_dat_top(10).py`

- クラス `TopologySection`（定義行 21）
- クラス `RmcPotDatTop`（定義行 33）
  - `__init__()`（定義行 56）
  - `path()`（定義行 93）
  - `clear()`（定義行 101）
  - `load()`（定義行 110）
  - `write()`（定義行 130）
  - `add_raw_line()`（定義行 149）
  - `add_comment()`（定義行 159）
  - `add_include()`（定義行 171）
  - `add_ifdef()`（定義行 180）
  - `add_ifndef()`（定義行 189）
  - `add_else()`（定義行 198）
  - `add_endif()`（定義行 206）
  - `add_section()`（定義行 214）
  - `get_sections()`（定義行 234）
  - `get_last_section()`（定義行 249）
  - `add_section_line()`（定義行 263）
  - `remove_sections()`（定義行 289）
  - `begin_molecule_type()`（定義行 303）
  - `add_atom()`（定義行 326）
  - `add_virtual_atom()`（定義行 368）
  - `add_pair()`（定義行 399）
  - `add_bond()`（定義行 426）
  - `add_angle()`（定義行 457）
  - `add_periodic_dihedral()`（定義行 490）
  - `add_harmonic_dihedral()`（定義行 524）
  - `add_rb_dihedral()`（定義行 556）
  - `add_exclusion()`（定義行 586）
  - `add_virtual_site2()`（定義行 608）
  - `add_virtual_site3()`（定義行 634）
  - `add_virtual_site4()`（定義行 669）
  - `set_system()`（定義行 702）
  - `set_molecules()`（定義行 714）
  - `add_molecule_template()`（定義行 734）
  - `add_explicit_network_molecule()`（定義行 807）
  - `validate_rmc_index_progression()`（定義行 848）
  - `validate()`（定義行 871）
- クラス `RmcPotDatItp`（定義行 1073）
- 関数 `main()`（定義行 1077）

## [`rmc_pot_fit`](rmc_pot_fit.md)

対象ソース: `rmc_pot_fit(7).py`

- クラス `RmcPotFit`（定義行 14）
  - `__init__()`（定義行 20）
  - `read_fit()`（定義行 59）
  - `get_S_calc()`（定義行 114）
  - `get_S_exp()`（定義行 136）
  - `get_S_exp_original()`（定義行 140）
  - `as_dict()`（定義行 144）

## [`rmc_pot_hst`](rmc_pot_hst.md)

対象ソース: `rmc_pot_hst(6).py`

- クラス `RmcPotHst`（定義行 39）
  - `__init__()`（定義行 41）
  - `read_chi2()`（定義行 202）
  - `detect_convergence()`（定義行 231）
  - `detect_convergence_set1()`（定義行 327）
  - `get_num_rmc_loops()`（定義行 368）
  - `get_generated()`（定義行 382）
  - `get_tried()`（定義行 413）
  - `get_accepted()`（定義行 441）
  - `get_time()`（定義行 469）
  - `get_tried_per_generated()`（定義行 497）
  - `get_accepted_per_tried()`（定義行 525）
  - `get_chi2_tot()`（定義行 553）
  - `get_chi2_set1()`（定義行 575）

## [`rmc_pot_log`](rmc_pot_log.md)

対象ソース: `rmc_pot_log(7).py`

- クラス `RmcPotLog`（定義行 19）
  - `__init__()`（定義行 21）
  - `load_log()`（定義行 65）
  - `set_cfg_name()`（定義行 99）
  - `get_cfg_name()`（定義行 109）
  - `is_finished()`（定義行 521）
  - `get_num_rmc_block()`（定義行 552）
  - `get_num_rmc_loop()`（定義行 560）
  - `get_generated()`（定義行 584）
  - `get_tried()`（定義行 594）
  - `get_accepted()`（定義行 604）
  - `get_chi2_tot()`（定義行 614）
  - `get_chi2_dataset()`（定義行 636）
  - `get_rw()`（定義行 657）
  - `get_tried_per_generated()`（定義行 663）
  - `get_accepted_per_tried()`（定義行 677）
  - `clear()`（定義行 695）
  - `remove_file()`（定義行 740）
  - `collect_result()`（定義行 759）
  - `backup_result()`（定義行 762）

## [`rmc_pot_ppcf`](rmc_pot_ppcf.md)

対象ソース: `rmc_pot_ppcf(9).py`

- クラス `RmcPotPpcf`（定義行 16）
  - `__init__()`（定義行 17）
  - `load()`（定義行 42）
  - `get_r()`（定義行 82）
  - `get_gij()`（定義行 85）
  - `get_single()`（定義行 88）
  - `get_labels()`（定義行 94）

## [`rmc_pot_snc`](rmc_pot_snc.md)

対象ソース: `rmc_pot_snc(3).py`

- クラス `RmcPotSnc`（定義行 14）
  - `__init__()`（定義行 17）
  - `load()`（定義行 27）
  - `get_qn_counts()`（定義行 69）
  - `get_common_qn_counts()`（定義行 82）

## [`runners_run_rmc`](runners_run_rmc.md)

対象ソース: `run_rmc(1).py`

- 関数 `run_rmc()`（定義行 11）

## [`util_cfg2poscar`](util_cfg2poscar.md)

対象ソース: `cfg2poscar(5).py`

- 関数 `parse_elements()`（定義行 42）
- 関数 `make_vasp_elements_line()`（定義行 87）
- 関数 `cfg2poscar()`（定義行 99）

## [`util_ensure_vasp5_format`](util_ensure_vasp5_format.md)

対象ソース: `ensure_vasp5_format(1).py`

- 関数 `ensure_vasp5_format()`（定義行 10）

## [`util_find_next_log_index`](util_find_next_log_index.md)

対象ソース: `find_next_log_index(20261116-081327).py`

- 関数 `next_log_dir_name()`（定義行 11）
- 関数 `find_next_log_index()`（定義行 94）

## [`util_gromacs_top_to_rmc_top`](util_gromacs_top_to_rmc_top.md)

対象ソース: `gromacs_top_to_rmc_top(2).py`

- クラス `TopologyConvertError`（定義行 47）
- クラス `GroAtom`（定義行 51）
  - `__init__()`（定義行 54）
- クラス `MoleculeType`（定義行 60）
  - `__init__()`（定義行 63）
- クラス `TopologyInfo`（定義行 69）
  - `__init__()`（定義行 72）
- 関数 `read_text_lines()`（定義行 109）
- 関数 `write_text_lines()`（定義行 115）
- 関数 `read_gro()`（定義行 125）
- 関数 `expand_local_includes()`（定義行 176）
- 関数 `parse_topology_info()`（定義行 239）
- 関数 `build_rmc_index_map()`（定義行 310）
- 関数 `replace_force_field_include()`（定義行 378）
- 関数 `convert_topology_lines()`（定義行 430）
- 関数 `convert_gromacs_top_to_rmc_top()`（定義行 489）
- 関数 `build_arg_parser()`（定義行 515）
- 関数 `main()`（定義行 544）

## [`util_poscar2cfg`](util_poscar2cfg.md)

対象ソース: `poscar2cfg(8).py`

- 関数 `contcar2cfg()`（定義行 42）
- 関数 `poscar2cfg()`（定義行 67）
- 関数 `vasp2cfg()`（定義行 98）
- 関数 `convert_to_cfg()`（定義行 137）

## [`util_zeolite`](util_zeolite.md)

対象ソース: `zeolite(2).py`

- クラス `ZeoliteCutoffs`（定義行 48）
  - `range_for_t()`（定義行 60）
- クラス `ZeoliteRmcConfig`（定義行 70）
- 関数 `load_zeolite_rmc_config_from_dat()`（定義行 137）
- 関数 `load_zeolite_rmc_config_from_init()`（定義行 259）
- 関数 `rmc_config_to_cutoffs()`（定義行 330）
- 関数 `find_rmc_parameter_source()`（定義行 343）
- 関数 `load_zeolite_rmc_config()`（定義行 376）
- クラス `ZeoliteCriteria`（定義行 395）
- クラス `PeriodicEdge`（定義行 413）
- 関数 `validate_framework_elements()`（定義行 452）
- 関数 `build_to_bonds()`（定義行 482）
- 関数 `coordination_distributions()`（定義行 542）
- 関数 `bond_length_statistics()`（定義行 652）
- 関数 `angle_statistics()`（定義行 679）
- 関数 `periodic_network_statistics()`（定義行 753）
- 関数 `build_tt_graph()`（定義行 834）
- 関数 `shortest_ring_statistics()`（定義行 901）
- 関数 `loewenstein_statistics()`（定義行 955）
- 関数 `framework_density()`（定義行 992）
- 関数 `evaluate_zeolite_like()`（定義行 998）
- 関数 `analyze_zeolite()`（定義行 1031）

