\echo (REQ:14) Le nom et le prix du manga le moins cher
select nom,prix from manga where prix = (select max(prix) from manga);
